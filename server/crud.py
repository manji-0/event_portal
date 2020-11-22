import datetime as dt
from sqlalchemy.orm import Session

from . import (
    models,
    schemas
)


def list_events_db(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()

def show_event_db(db: Session, event_id: str):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    participants = db.query(models.Event).filter(models.Event.id == event_id).first()

    return {'event': event, 'participants': participants}

def create_event_db(db: Session, event: schemas.PostEvent, uuid: str):
    db_event = models.Event(**event.dict(), id=uuid)
    db.add(db_event)
    db.commit()
    db.refresh()
    return db_event

def update_event_db(db: Session, event_id: str, data: schemas.PatchEvent):
    target = db.query(models.Event).filter(models.Event.id == event_id).first()
    target.update(**data.dict())
    db.commit()
    db.refresh()

    return target

def delete_event_db(db: Session, event_id: str):
    target = db.query(models.Event).filter(models.Event.id == event_id).first()
    db.delete(target)
    db.commit()
    return True

def add_participants_to_event_db(db: Session, event_id: str, email: str):
    db_item = models.Participants(event_id=event_id, email=email)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_participants_from_event_db(db: Session, event_id: str, email: str):
    target = db.query(models.Participants).filter(models.Participants.email == email and models.Participants.event_id == event_id).first()
    db.delete(target)
    db.commit()
    return True
