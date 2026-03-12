from pathlib import Path
from ultralytics import YOLO
import numpy as np

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "defect_detector.pt"

_model: YOLO | None = None


def get_model() -> YOLO:
    global _model
    if _model is None:
        _model = YOLO(str(MODEL_PATH))
    return _model


def detect_defects(image: np.ndarray) -> dict:
    model = get_model()
    results = model(image, verbose=False)
    result = results[0]

    detections = []
    boxes = result.boxes
    for i in range(len(boxes)):
        x1, y1, x2, y2 = boxes.xyxy[i].tolist()
        conf = float(boxes.conf[i])
        cls_idx = int(boxes.cls[i])
        label = result.names[cls_idx]

        detections.append({
            "label": label,
            "confidence": round(conf, 4),
            "bbox": [round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1)],
        })

    return {
        "detections": detections,
        "image_width": image.shape[1],
        "image_height": image.shape[0],
    }
