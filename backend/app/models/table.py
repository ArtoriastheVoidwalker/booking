import enum


from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class DocEnum(enum.Enum):
    def __new__(cls, value, doc=None):
        self = object.__new__(cls)
        self._value_ = value
        if doc is not None:
            self.__doc__ = doc
        return self


class TableStatus(DocEnum):
    is_free = 'is_free'
    booked = 'booked'
    not_available = 'not_available'


class TableType(DocEnum):
    common = 'common'
    cabin = 'cabin'
    room = 'room'


class Table(Base):
    id = Column(Integer, primary_key=True, index=True)
    site = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    table_status = Column(Enum(TableStatus), nullable=False)
    table_type = Column(Enum(TableType), nullable=False)
    bookings = relationship("Booking", back_populates="table")


