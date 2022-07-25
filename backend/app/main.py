import logging
import logging.config

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.logger_config import LOG_CONFIG
from app.api.api_v1.api import api_router
from app.core.config import settings

import coloredlogs


coloredlogs.install()
logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)
logger.info(f'Redoc url: {settings.SERVER_HOST}/redoc')

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# app.mount("/storage", StaticFiles(directory="storage"), name="static")

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.add_middleware(SessionMiddleware, secret_key=f'{settings.SESSION_SECRET}')
app.include_router(api_router, prefix=settings.API_V1_STR)
