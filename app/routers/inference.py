from fastapi import APIRouter, UploadFile, File
from app.services.model_runner import predict

router = APIRouter(prefix="/predict", tags=["inference"])


@router.post("/")
async def predict_image(file: UploadFile = File(...)):
    contents = await file.read()
    # Save file temporarily for processing
    with open("temp_image.jpg", "wb") as f:
        f.write(contents)
    result = predict("temp_image.jpg")
    return {"prediction": result}
