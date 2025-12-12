from .questions_config import QUESTIONS

# Dimensions from PDF
DIMENSIONS = ["business_fit", "leadership", "workforce", "data", "adoption"]


# Scoring map for single-choice questions (1–5 scale)
CHOICE_SCORES = {
    "Immediate": 5,
    "High Priority": 4,
    "Medium Priority": 3,
    "Low Priority": 2,

    "Strong team": 5,
    "Basic knowledge": 3,
    "Exploring": 2,
    "None": 1,

    "On-prem": 2,
    "Hybrid": 4,
    "Cloud": 5,

    "Yes": 5,
    "No": 1,
    "Experimenting": 3,
}


def score_multi_choice(selected_list, options):
    """
    Multi-choice scoring: Scale based on ratio of selected options.
    1 -> minimum
    5 -> maximum
    """
    if not selected_list:
        return 1   # minimum readiness score

    ratio = min(len(selected_list), len(options)) / len(options)
    return round(1 + ratio * 4, 2)   # ratio=0→1, ratio=1→5


def compute_dimension_scores(answers: dict):
    """
    Compute weighted average per dimension.
    All rating questions use 1–5.
    Single-choice is mapped to 1–5.
    Multi-choice converts selection ratio to 1–5.
    """
    totals = {d: 0.0 for d in DIMENSIONS}
    weights = {d: 0.0 for d in DIMENSIONS}

    # build lookup
    QMAP = {q["id"]: q for q in QUESTIONS}

    for qid, value in answers.items():
        q = QMAP.get(qid)
        if not q or "dimension" not in q:
            continue

        dim = q["dimension"]
        weight = q.get("weight", 1.0)
        q_type = q["type"]

        score = None

        # --- Rating ---
        if q_type == "rating":
            score = float(value)
            if q.get("invert"):
                score = 6 - score  # reverse 1–5 to 5–1

        # --- Single-choice ---
        elif q_type == "single_choice":
            score = CHOICE_SCORES.get(value, 1)

        # --- Multi-choice ---
        elif q_type == "multi_choice":
            score = score_multi_choice(value, q["options"])

        if score is not None:
            totals[dim] += score * weight
            weights[dim] += weight

    # Compute weighted averages
    final_scores = {}
    for dim in DIMENSIONS:
        final_scores[dim] = (
            round(totals[dim] / weights[dim], 2) if weights[dim] else 1.0
        )

    return final_scores



def compute_overall_score(dim_scores: dict):
    """
    Convert average (1–5) → percentage (0–100) → capped (40–80)
    PDF Model:
        1 → 0%
        3 → 50%
        5 → 100%
    Then apply mandatory capping:
        < 40 → 40
        > 80 → 80
    """
    if not dim_scores:
        return 40.0  # lowest possible per PDF

    avg_score = sum(dim_scores.values()) / len(dim_scores)  # still 1–5 scale

    # Convert 1–5 to 0–100%
    percent = ((avg_score - 1) / 4) * 100
    percent = round(percent, 1)

    # Capping rules
    if percent < 40:
        percent = 40.0
    elif percent > 80:
        percent = 80.0

    return percent



def get_category(score):
    """
    PDF-aligned category buckets:
    40–49  = AI Aspirant
    50–59  = AI Explorer
    60–69  = AI Adopter
    70–80  = AI Transformer
    """
    if score < 50:
        return "AI Aspirant"
    elif score < 60:
        return "AI Explorer"
    elif score < 70:
        return "AI Adopter"
    else:
        return "AI Transformer"
