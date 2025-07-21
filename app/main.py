from fastapi import FastAPI
from app.routers import inference
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="PerceptiFlow Inference API")

app.include_router(inference.router)

# Prometheus metrics endpoint
Instrumentator().instrument(app).expose(app)


@app.get("/")
async def root():
    return {"message": "Welcome to PerceptiFlow API"}
