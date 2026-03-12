import numpy as np
from app.services.classifier import classify_produce
from app.services.defect_detector import detect_defects
from app.services.area_calculator import compute_defect_percentage
from app.services.grading_engine import determine_grade


def _crop_to_bbox(image: np.ndarray, bbox: list) -> np.ndarray:
    x1, y1, x2, y2 = [int(v) for v in bbox]
    h, w = image.shape[:2]
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(w, x2), min(h, y2)
    return image[y1:y2, x1:x2]


def run_pipeline(image: np.ndarray) -> dict:
    classification = classify_produce(image)

    # No object detected at all — return early with unknown
    if not classification["bbox"]:
        grading = determine_grade(0.0)
        return {
            "produce": "unknown",
            "confidence": 0.0,
            "defect_percentage": 0.0,
            "grade": grading["grade"],
            "label": grading["label"],
            "defects": [],
        }

    # Crop detected fruit region and run defect detection on the crop
    cropped = _crop_to_bbox(image, classification["bbox"])
    detection = detect_defects(cropped)

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
