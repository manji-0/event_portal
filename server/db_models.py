from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    CHAR,
    NVARCHAR,
    DATETIME
    ) 
from sqlalchemy.orm import relationship

from .db import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(CHAR(length=36), primary_key=True, index=True)
    name = Column(NVARCHAR(length=128))
    location = Column(NVARCHAR(length=256))
    state_time = Column(DATETIME)
    end_time = Column(DATETIME)

    participants = relationship("Participants", back_populates="event")

class Participants(Base):
    __tablename__ = "participants"

    id = Column(Integer, unique=True)
    email = Column(NVARCHAR(length=320))
    event_id = Column(CHAR(length=36), ForeignKey("events.id"))

    event = relationship("Event", back_populates="participants")
