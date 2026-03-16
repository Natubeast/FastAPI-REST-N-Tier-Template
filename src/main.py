from fastapi import FastAPI
from .routers.users import user_router

app = FastAPI(title="FastAPI N-Tier Template")
# Include routers
app.include_router(user_router.router, prefix="/api/v1")