from fastapi import APIRouter, HTTPException

router = APIRouter()

# Basic health check. Expand on this once other services are implemented.
@router.get("/", tags=["Health"])
def health_check():
    return {"status": "running"}