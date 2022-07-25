from typing import Optional, List
from pydantic import BaseModel
from app.models.booking import BookingStatus



class BookingBase(BaseModel):
    email: str = None
    phone: str


class BookingCreate(BaseModel):
    email: str = None
    phone: str
    # status: BookingStatus = 'in_processing'
    table_id: int




class BookingUpdate(BaseModel):
    status: BookingStatus


class BookingInDBBase(BookingBase):
    id: Optional[int]

    class Config:
        orm_mode = True


class Booking(BookingInDBBase):
    pass


class Bookings(BaseModel):
    booking: List[Booking] = []
    amount: Optional[int]
