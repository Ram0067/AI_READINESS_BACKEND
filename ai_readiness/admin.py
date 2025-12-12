from django.contrib import admin
from .models import Assessment, Answer, Question


# Inline to show answers inside Assessment page
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    readonly_fields = ("question", "raw_value", "value_numeric")
    fields = ("question", "raw_value", "value_numeric")
    can_delete = False


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ("email", "company_name", "category", "overall_score", "created_at")
    search_fields = ("email", "company_name", "category")
    list_filter = ("category", "created_at")

    readonly_fields = (
        "person_name",
        "company_name",
        "email",
        "phone",
        "designation",
        "overall_score",
        "category",
        "dimension_scores",
        "feedback_summary",
        "feedback_profile",
        "feedback_category_detail",
        "feedback_recommended_actions",
        "raw_score",
        "created_at",
        "updated_at",
    )

    inlines = [AnswerInline]

    fieldsets = (
        ("Client Details", {
            "fields": ("person_name", "company_name", "email", "phone", "designation")
        }),
        ("AI Readiness Score & Category", {
            "fields": ("overall_score", "category", "dimension_scores")
        }),
        ("Narrative Insights", {
            "fields": (
                "feedback_summary",
                "feedback_profile",
                "feedback_category_detail",
                "feedback_recommended_actions",
            )
        }),
        ("System Metadata", {
            "fields": ("raw_score", "created_at", "updated_at")
        }),
    )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "assessment", "question", "raw_value", "value_numeric")
    readonly_fields = ("assessment", "question", "raw_value", "value_numeric")
    search_fields = ("assessment__email", "question__key", "question__text")
    list_filter = ("question__section",)
