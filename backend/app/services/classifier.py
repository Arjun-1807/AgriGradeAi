from pathlib import Path
from ultralytics import YOLO
import numpy as np

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "produce_classifier.pt"

_model: YOLO | None = None


def get_model() -> YOLO:
    global _model
    if _model is None:
        _model = YOLO(str(MODEL_PATH))
    return _model


def classify_produce(image: np.ndarray) -> dict:
    model = get_model()
    results = model(image, verbose=False)
    result = results[0]

    top_class_idx = int(result.probs.top1)
    confidence = float(result.probs.top1conf)
    class_name = result.names[top_class_idx]

    return {
        "produce": class_name,
        "confidence": round(confidence, 4),
    }
