import os


class Settings:
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    MODEL_PATH = os.getenv("MODEL_PATH", "./models/model.pt")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
