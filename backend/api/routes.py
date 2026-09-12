from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/api")


class SolveRequest(BaseModel):
    issue: str
    location: str


@router.post("/solve")
def solve_issue(request: SolveRequest):
    return {
        "success": True,
        "message": "CampusFix API is working.",
        "data": {
            "issue": request.issue,
            "location": request.location,
            "status": "received",
        },
    }