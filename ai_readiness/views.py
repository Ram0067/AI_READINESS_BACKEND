from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .questions_config import QUESTIONS
from .serializers import AssessmentCreateSerializer
from .models import Assessment

class QuestionsView(APIView):
    """
    GET /api/ai-readiness/questions/
    Returns questions for dynamic form rendering.
    """
    def get(self, request):
        # Return the QUESTIONS config the frontend expects
        return Response({"questions": QUESTIONS}, status=status.HTTP_200_OK)


class SubmitAssessmentView(APIView):
    """
    POST /api/ai-readiness/submit/
    Save answers + return scoring & feedback
    """
    def post(self, request):
        serializer = AssessmentCreateSerializer(data=request.data)
        if serializer.is_valid():
            assessment = serializer.save()
            return Response(
                {
                    "assessment_id": str(assessment.id),
                    "email": assessment.email,
                    "overall_score": assessment.overall_score,
                    "category": assessment.category,
                    "dimension_scores": assessment.dimension_scores,
                    "feedback_summary": assessment.feedback_summary,
                    "feedback_profile": assessment.feedback_profile,
                    "feedback_category_detail": assessment.feedback_category_detail,
                    "recommended_actions": assessment.feedback_recommended_actions,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
