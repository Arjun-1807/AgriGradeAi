from pathlib import Path
from ultralytics import YOLO
import numpy as np

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "produce_detector.pt"

_model: YOLO | None = None


def get_model() -> YOLO:
    global _model
    if _model is None:
        _model = YOLO(str(MODEL_PATH))
    return _model


def classify_produce(image: np.ndarray) -> dict:
    model = get_model()
    results = model(image, verbose=False)
    boxes = results[0].boxes

    if len(boxes) == 0:
        return {"produce": "unknown", "confidence": 0.0, "bbox": []}

    # Pick the detection with the largest bounding box area
    xyxy = boxes.xyxy
    areas = (xyxy[:, 2] - xyxy[:, 0]) * (xyxy[:, 3] - xyxy[:, 1])
    best_idx = int(areas.argmax())

    class_id = int(boxes.cls[best_idx])
    confidence = float(boxes.conf[best_idx])
    produce = model.names[class_id]
    x1, y1, x2, y2 = xyxy[best_idx].tolist()

    if confidence < 0.40:
        produce = "unknown"

    return {
        "produce": produce,
        "confidence": round(confidence, 4),
        "bbox": [round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1)],
    }
