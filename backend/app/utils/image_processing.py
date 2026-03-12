from PIL import Image
import io
import numpy as np


SUPPORTED_FORMATS = {"image/jpeg", "image/png", "image/webp"}
MAX_SIZE = 10 * 1024 * 1024


def validate_image(file_bytes: bytes, content_type: str) -> None:
    if content_type not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported image format: {content_type}")
    if len(file_bytes) > MAX_SIZE:
        raise ValueError("Image exceeds 10 MB size limit")


def load_image(file_bytes: bytes) -> np.ndarray:
    image = Image.open(io.BytesIO(file_bytes)).convert("RGB")
    return np.array(image)
