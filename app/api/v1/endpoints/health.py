"""Health check endpoints."""

from typing import Dict

from fastapi import APIRouter, status

from app.core.config import settings

router = APIRouter()


@router.get(
    "/",
    response_model=Dict[str, str],
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Check if the service is running",
)
async def health_check() -> Dict[str, str]:
    """Basic health check endpoint."""
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
    }


@router.get(
    "/ready",
    response_model=Dict[str, bool],
    status_code=status.HTTP_200_OK,
    summary="Readiness Check",
    description="Check if the service is ready to handle requests",
)
async def readiness_check() -> Dict[str, bool]:
    """Readiness check for dependencies."""
    # TODO: Check database connection
    # TODO: Check Redis connection
    # TODO: Check AI provider availability
    
    return {
        "database": True,  # Placeholder
        "cache": True,     # Placeholder
        "ai_provider": True,  # Placeholder
    }