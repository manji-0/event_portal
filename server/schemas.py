from typing import List

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import UUID4

from pydantic import constr


# Request Body
## Events
class PostEvent(BaseModel):
    name = constr(min_length=1, max_length=128)
    location = constr(min_length=1, max_length=256)
    start_timestamp = constr(regex=r"[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]")
    end_timestamp = constr(regex=r"[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]")

class PatchEvent(BaseModel):
    name: str = Field(None, min_length=1, max_length=128)
    location: str = Field(None, min_length=1, max_length=256)
    start_timestamp: str = Field(
        None,
        regex=r"[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]"
    )
    end_timestamp: str = Field(
        None,
        regex=r"[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]"
    )

class DeleteEvent(BaseModel):
    pass

class PostSignUpEvent(BaseModel):
    email = EmailStr

class PostCancelParticipateEvent(BaseModel):
    email = EmailStr

# Response Body
class Event(BaseModel):
    name: str
    _id: str
    location: str

    class Config:
        fields = {'_id': 'id'}

class EventDetail(BaseModel):
    name: str
    _id: str
    location: str
    start_time: str
    end_time: str

class ListEvents(BaseModel):
    events: List[Event]

class ShowEvent(BaseModel):
    event: EventDetail
    participants: List[EmailStr]

class CreateEvents(BaseModel):
    event: EventDetail

class ListParticipants(BaseModel):
    participants: List[EmailStr]
