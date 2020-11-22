from fastapi import APIRouter
from pydantic import BaseModel
from pydantic import Field
from typing import Optional
from .. import db
from .. import schemas

router = APIRouter()


class Message(BaseModel):
    status: str = Field("", description="status description")
    message: str = Field("", description="detail of the status")

@router.get("/", response_model=schemas.ListEvents)
async def list_events():
    pass

@router.get(
    "/{event_id}",
    responses={
        200: {'model': schemas.ShowEvent},
        404: {'model': Message}})
async def show_event():
    pass

@router.post(
    "/",
    responses={
        201: {'model': schemas.CreateEvent},
        400: {'model': Message},
        401: {'model': Message},
        403: {'model': Message},
        409: {'model': Message}})
async def create_event(body: schemas.PostEvent):
    pass

@router.patch(
    "/{event_id}",
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

