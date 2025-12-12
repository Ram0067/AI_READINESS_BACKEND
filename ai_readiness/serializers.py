from rest_framework import serializers
from .models import Assessment, Answer, Question
from .questions_config import QUESTIONS
from .scoring import compute_dimension_scores, compute_overall_score
from .feedback import generate_feedback

# Build lookup map
QUESTION_INDEX = {q["id"]: q for q in QUESTIONS}
REQUIRED_QUESTION_IDS = set(QUESTION_INDEX.keys())


class AssessmentCreateSerializer(serializers.Serializer):
    person_name = serializers.CharField(required=False, allow_blank=True)
    company_name = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField()
    phone = serializers.CharField(required=False, allow_blank=True)
    designation = serializers.CharField(required=False, allow_blank=True)
    answers = serializers.DictField(child=serializers.JSONField())

    def validate(self, data):
        answers = data.get("answers", {})
        if not isinstance(answers, dict) or not answers:
            raise serializers.ValidationError("Answers must be a non-empty dictionary.")

        # Validate IDs
        received_ids = set(answers.keys())
        unknown = received_ids - REQUIRED_QUESTION_IDS
        missing = REQUIRED_QUESTION_IDS - received_ids

        if unknown:
            raise serializers.ValidationError(f"Unknown question IDs: {sorted(list(unknown))}")

        if missing:
            raise serializers.ValidationError(f"Missing required questions: {sorted(list(missing))}")

        # Validate each question by type
        for qid, raw_value in answers.items():
            q = QUESTION_INDEX[qid]
            q_type = q["type"]

            # Rating validation (STRICT 1–5)
            if q_type == "rating":
                try:
                    num = int(raw_value)
                except ValueError:
                    raise serializers.ValidationError(f"{qid} must be a number between 1 and 5.")

                if num < 1 or num > 5:
                    raise serializers.ValidationError(f"{qid} must be a number between 1 and 5.")

            # Single-choice validation
            elif q_type == "single_choice":
                if raw_value not in q["options"]:
                    raise serializers.ValidationError(
                        f"{qid} must be one of {q['options']}"
                    )

            # Multi-choice validation
            elif q_type == "multi_choice":
                if not isinstance(raw_value, list):
                    raise serializers.ValidationError(f"{qid} must be a list of options.")
                for item in raw_value:
                    if item not in q["options"]:
                        raise serializers.ValidationError(f"Invalid option '{item}' in {qid}.")

            # Text questions → no validation needed

        return data

    def create(self, validated_data):
        person_name = validated_data.get("person_name", "")
        company_name = validated_data.get("company_name", "")
        email = validated_data["email"]
        phone = validated_data.get("phone", "")
        designation = validated_data.get("designation", "")
        answers = validated_data["answers"]

        # Create assessment
        assessment = Assessment.objects.create(
            person_name=person_name,
            company_name=company_name,
            email=email,
            phone=phone,
            designation=designation,
        )

        # Store individual answers
        for qid, raw_value in answers.items():
            q_config = QUESTION_INDEX[qid]

            question_obj, _ = Question.objects.get_or_create(
                key=qid,
                defaults={
                    "text": q_config["label"],
                    "section": q_config["section"],
                }
            )

            # numeric value for scoring (only rating type)
            value_numeric = None
            if q_config["type"] == "rating":
                value_numeric = float(raw_value)

            Answer.objects.create(
                assessment=assessment,
                question=question_obj,
                raw_value=raw_value,
                value_numeric=value_numeric,
            )

        # Compute scores
        dim_scores = compute_dimension_scores(answers)
        overall_score = compute_overall_score(dim_scores)

        # Generate feedback
        feedback = generate_feedback(dim_scores, overall_score)

        # Save results in Assessment
        assessment.raw_score = sum([a.value_numeric or 0 for a in assessment.answers.all()])
        assessment.dimension_scores = dim_scores
        assessment.overall_score = overall_score
        assessment.category = feedback["category"]
        assessment.feedback_summary = feedback["summary"]
        assessment.feedback_profile = feedback["profile"]
        assessment.feedback_category_detail = feedback["category_detail"]
        assessment.feedback_recommended_actions = feedback["recommended_actions"]
        assessment.save()

        return assessment
