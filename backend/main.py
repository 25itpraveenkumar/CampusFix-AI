from fastapi import FastAPI

from backend.api.routes import router


app = FastAPI(
    title="CampusFix AI",
    description="Simulated campus issue resolution backend",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "success": True,
        "message": "CampusFix AI backend is running.",
    }