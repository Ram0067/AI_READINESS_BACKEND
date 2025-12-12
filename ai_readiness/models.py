import uuid
from django.db import models
from django.utils import timezone

class Question(models.Model):
    # If you prefer single source of truth, you can seed this from QUESTIONS
    key = models.CharField(max_length=32, unique=True)  # e.g., "A1", "B4"
    text = models.TextField()
    section = models.CharField(max_length=64, blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.key}: {self.text[:60]}"


class Assessment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # contact / meta
    person_name = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)

    # raw / computed
    raw_score = models.FloatField(default=0.0)          # sum of numeric answers if applicable
    raw_percent = models.FloatField(default=0.0)        # normalized 0..100 if you use normalization
    capped_percent = models.FloatField(default=0.0)     # final value after PDF capping rules
    overall_score = models.FloatField(default=0.0)      # the "overall" percent your serializer expects
    category = models.CharField(max_length=64, blank=True, null=True)

    # store dimension scores and rich feedback
    dimension_scores = models.JSONField(default=dict, blank=True)
    feedback_summary = models.TextField(blank=True, null=True)
    feedback_profile = models.TextField(blank=True, null=True)
    feedback_category_detail = models.TextField(blank=True, null=True)
    feedback_recommended_actions = models.JSONField(default=list, blank=True)

    extra = models.JSONField(default=dict, blank=True)  # store additional form fields

    def __str__(self):
        return f"Assessment #{self.id} ({self.email})"


class Answer(models.Model):
    """
    Stores each answer for a given assessment.
    One row per question per submission.
    """
    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE,
        related_name="answers",
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.PROTECT,
        related_name="answers",
    )

    # raw_value holds whatever was submitted (string/list/number)
    raw_value = models.JSONField()

    # for numeric tasks (ratings), keep a numeric value we can sum/aggregate
    value_numeric = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("assessment", "question")
        indexes = [
            models.Index(fields=["assessment", "question"]),
        ]

    def __str__(self):
        return f"Answer: {self.question.key} -> {self.raw_value} (assmnt {self.assessment_id})"
