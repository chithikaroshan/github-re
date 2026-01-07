from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.routes import router
from app.db.models import Base
from app.db.session import engine
from app.core.exceptions import ExternalServiceUnavailableException

# Create database tables
Base.metadata.create_all(bind=engine)

# 🔴 THIS LINE IS MANDATORY
app = FastAPI(title="GitHub Repo Service")

@app.exception_handler(ExternalServiceUnavailableException)
async def external_api_exception(_, exc):
    return JSONResponse(
        status_code=503,
        content={"detail": str(exc)}
    )

app.include_router(router)
