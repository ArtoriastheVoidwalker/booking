import enum

from datetime import datetime as dt
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class DocEnum(enum.Enum):
    def __new__(cls, value, doc=None):
        self = object.__new__(cls)
        self._value_ = value
        if doc is not None:
            self.__doc__ = doc
        return self


class BookingStatus(DocEnum):
    in_processing = 'in_processing'
    accepted = 'accepted'
    reject = 'reject'
    cancel = 'cancel'


class Booking(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    status = Column(Enum(BookingStatus), nullable=False)
    created_at = Column(DateTime, nullable=False, default=dt.now)

    table = relationship("Table", back_populates="bookings")
    table_id = Column(Integer, ForeignKey("table.id"), nullable=True)
