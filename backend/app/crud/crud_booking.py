from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models import Booking
from app.schemas import BookingCreate, BookingUpdate
from datetime import datetime as dt

from sqlalchemy.orm import Session


class CRUDBooking(CRUDBase[Booking, BookingCreate, BookingUpdate]):

    def get_by_table(self, db: Session, *, table_id: str) -> Optional[Booking]:
        return db.query(Booking).filter(Booking.table_id == table_id).first()


    def create(self, db: Session, *, obj_in: BookingCreate) -> Booking:

        db_obj = Booking(
            email=obj_in.email,
            phone=obj_in.phone,
            status='in_processing',
            created_at=dt.now(),
            table_id=obj_in.table_id
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


    def update(
        self, db: Session, *, booking_id: int, obj_in: Union[BookingUpdate, Dict[str, Any]]
    ) -> Booking:

        db_obj = self.get(db, id=booking_id)

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


booking = CRUDBooking(Booking)
