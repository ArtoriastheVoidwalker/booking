from pydantic import BaseModel
from typing import Optional

from .table import Table, TableCreate, Tables, TableUpdate
from .booking import Booking, BookingCreate, Bookings, BookingUpdate

# from .user import (
#     User, Users, UserCreate, UserUpdate,
#     UserLogin, ValidateCode
# )

class DefaultResponseSchema(BaseModel):

    status_code: Optional[int] = 200
    success: Optional[bool] = True
