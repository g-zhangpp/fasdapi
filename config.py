import os
from typing import List

from pydantic import BaseSettings

class Config(BaseSettings):
    APP_DEBUG: bool = True

    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "fasdapi"
    DESCRIPTION: str = "fasdapi"

    STATIC_DIR: str = os.path.join(os.getcwd(), "../static")

    CORS_ORIGINS: List[str] = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_HEADERS: List[str] = ["*"]
    CORS_ALLOW_METHODS: List[str] = ["*"]

settings = Config()