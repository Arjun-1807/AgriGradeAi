import cv2
import numpy as np


def detect_defects_heuristic(image: np.ndarray) -> float:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    # Create fruit mask to isolate fruit from background
    fruit_mask = (s > 40) & (v > 50)
    kernel = np.ones((5, 5), np.uint8)
    fruit_mask = cv2.morphologyEx(fruit_mask.astype(np.uint8) * 255, cv2.MORPH_CLOSE, kernel)

    fruit_pixels = int(np.sum(fruit_mask > 0))
    if fruit_pixels == 0:
        return 0.0

    # Detect defect regions
    dark_mask = v < 80
    low_sat_mask = s < 40
    defect_mask = (dark_mask | low_sat_mask) & (fruit_mask > 0)

    defect_pixels = int(np.sum(defect_mask))
    defect_percentage = (defect_pixels / fruit_pixels) * 100

    return round(min(defect_percentage, 100.0), 2)
