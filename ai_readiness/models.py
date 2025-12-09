import uuid
from django.db import models
from django.utils import timezone


class Assessment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Lead for sales team
    email = models.EmailField(db_index=True)

    # Scores saved after calculation
    overall_score = models.DecimalField(
    max_digits=5, decimal_places=1, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)

    # Breakdown (JSON) e.g. {"data": 6.2, "adoption": 6.7, ...}
    dimension_scores = models.JSONField(null=True, blank=True)

    # AI feedback strings
    feedback_summary = models.TextField(null=True, blank=True)
    feedback_profile = models.TextField(null=True, blank=True)
    feedback_category_detail = models.TextField(null=True, blank=True)
    feedback_recommended_actions = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email} – {self.category or 'Pending'}"


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

    question_id = models.CharField(max_length=10)
    section = models.CharField(max_length=50)
    question_text = models.TextField()
    answer_type = models.CharField(max_length=20)
    raw_value = models.JSONField()

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("assessment", "question_id")

    def __str__(self):
        return f"{self.assessment.email} – {self.question_id}"
