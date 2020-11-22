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
@app.head("/")
async def healthcheck():
    return
