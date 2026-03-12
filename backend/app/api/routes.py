from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel

from app.utils.image_processing import validate_image, load_image
from app.services.pipeline import run_pipeline


router = APIRouter()


class DefectDetail(BaseModel):
    label: str
    confidence: float
    bbox: list[float]


class GradeResponse(BaseModel):
    produce: str
    confidence: float
    defect_percentage: float
    grade: str
    label: str
    defects: list[DefectDetail]


@router.post("/grade", response_model=GradeResponse)
async def grade_produce(file: UploadFile = File(...)):
    file_bytes = await file.read()

    try:
        validate_image(file_bytes, file.content_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    image = load_image(file_bytes)
    result = run_pipeline(image)
    return result
