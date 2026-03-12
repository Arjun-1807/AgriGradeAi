import numpy as np
from app.services.classifier import classify_produce
from app.services.defect_detector import detect_defects
from app.services.area_calculator import compute_defect_percentage
from app.services.grading_engine import determine_grade


def run_pipeline(image: np.ndarray) -> dict:
    classification = classify_produce(image)
    detection = detect_defects(image)

    defect_pct = compute_defect_percentage(
        detection["detections"],
        detection["image_width"],
        detection["image_height"],
    )

    grading = determine_grade(defect_pct)

    return {
        "produce": classification["produce"],
        "confidence": classification["confidence"],
        "defect_percentage": defect_pct,
        "grade": grading["grade"],
        "label": grading["label"],
        "defects": detection["detections"],
    }
