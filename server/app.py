from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from .routers import events
from .routers import users


app = FastAPI()

# Routes
app.include_router(
    events.router,
    prefix="/v1/events"
    )

# General Routes
@app.get("/", tags=["Service Health Check"])
async def selfcheck():
    return {
        "ping": "pong",
        "version": "0.1.0",
        "api_version": "v1"}


