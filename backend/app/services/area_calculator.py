FRESH_LABELS = {"fresh"}


def compute_defect_percentage(detections: list, image_width: int, image_height: int) -> float:
    image_area = image_width * image_height
    if image_area == 0:
        return 0.0

    defect_area = 0.0
    for det in detections:
        if det["label"].lower() in FRESH_LABELS:
            continue
        x1, y1, x2, y2 = det["bbox"]
        box_area = max(0, x2 - x1) * max(0, y2 - y1)
        defect_area += box_area

    percentage = (defect_area / image_area) * 100
    return round(min(percentage, 100.0), 2)
