from fastapi import FastAPI, HTTPException
from api import router as api_router  
from database import SessionLocal, Base, engine
from api.models import Letter
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    if db.query(Letter).count() == 0:
        data = [
            {"letter": "A", "value": 1, "strokes": 2, "vowel": True},
            {"letter": "B", "value": 2, "strokes": 1, "vowel": False},
        ]
        for item in data:
            db.add(Letter(**item))
        db.commit()
    db.close()

    yield


app = FastAPI(
     title="Enstack",
    description="Looking forward to being hired.",
    version="1.0.0",
    lifespan=lifespan
)

Base.metadata.create_all(bind=engine)


app.include_router(api_router, prefix="/api", tags=["Api"])
