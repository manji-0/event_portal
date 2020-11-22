from fastapi import (
    APIRouter,
    Depends,
    HTTPException
    )
from pydantic import BaseModel
from pydantic import Field
from typing import Optional
from sqlalchemy.orm import Session

from ..db import SessionLocal, engine

from .. import (
    crud,
    models,
    schemas
)

models.Base.metadata.create_all(bind=engine)


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Message(BaseModel):
    detail: str

@router.get("/", response_model=schemas.ListEvents)
async def list_events(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100):
    events = crud.list_events_db(db=db, skip=skip, limit=limit)
    return events

@router.get(
    "/{event_id}",
    responses={
        200: {'model': schemas.ShowEvent},
        404: {'model': Message}})
async def show_event(
    event_id: str,
    db: Session = Depends(get_db)):
    event = crud.show_event_db(db, event_id)
    return event

@router.post(
    "/",
    status_code=201,
    responses={
        201: {'model': schemas.CreateEvent},
        400: {'model': Message},
        401: {'model': Message},
        403: {'model': Message},
        409: {'model': Message}})
async def create_event(
    body: schemas.PostEvent,
    db: Session = Depends(get_db)):
    result = crud.create_event_db(db, body)

    if result:
        return result
    else:
        raise HTTPException(503)

@router.patch(
    "/{event_id}",
    status_code=200,
    responses={
        200: {'model': schemas.CreateEvent},
        400: {'model': Message},
        401: {'model': Message},
        403: {'model': Message},
        404: {'model': Message}})
async def edit_event(body: schemas.PatchEvent):
    pass

@router.delete(
    "/{event_id}",
    status_code=204,
    responses={
        204: {},
        404: {'model': Message},
        409: {'model': Message}})
async def delete_event():
    pass    

@router.get(
    "/{event_id}/participant",
    responses={
        200: {'model': Message},
        404: {'model': Message}})
async def list_event_participant():
    pass

@router.post(
    "/{event_id}/participant",
    responses={
        200: {'model': Message},
        404: {'model': Message}})
async def signup_event():
    pass

@router.post(
    "/{event_id}/cancellation",
    responses={
        200: {'model': Message},
        404: {'model': Message}})
async def cancel_paticipate_event():
    pass

