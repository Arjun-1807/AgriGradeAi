GRADE_THRESHOLDS = [
    {"max_defect": 5, "grade": "A", "label": "Premium Quality"},
    {"max_defect": 15, "grade": "B", "label": "Standard Quality"},
    {"max_defect": 30, "grade": "C", "label": "Below Standard"},
]

REJECT = {"grade": "Reject", "label": "Rejected"}


def determine_grade(defect_percentage: float) -> dict:
    for threshold in GRADE_THRESHOLDS:
        if defect_percentage < threshold["max_defect"]:
            return {"grade": threshold["grade"], "label": threshold["label"]}
    return {**REJECT}
