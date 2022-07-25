from typing import Any, List
from datetime import datetime as datatime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps


router = APIRouter()


@router.post("/booking", response_model=schemas.Booking)
async def create_booking(
    *,
    db: Session = Depends(deps.get_db),
    booking_data: schemas.BookingCreate,
    # current_user: Optional[models.User] = Depends(deps.get_current_active_user)
) -> Any:
    if crud.table.get(db=db, id=booking_data.table_id) is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return crud.booking.create(db, obj_in=booking_data)


@router.patch("/booking/{id}", response_model=schemas.Booking)
async def cancel(
    *,
    id: int,
    db: Session = Depends(deps.get_db),
    # current_moderator: models.Moderator = Depends(deps.get_current_active_admin)
):
    booking = crud.booking.get(db, id=id)

    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    table = crud.table.get(db=db, id=booking.table_id)
    crud.table.update(db=db, id=table.id, obj_in={"table_status":"is_free"})

    return crud.booking.update(db, booking_id=id, obj_in={"status":"cancel"})


@router.get("/tables", response_model=schemas.Tables)
async def get_tables(
    min_price: int,
    max_price: int,
    site: int,
    table_type: str,
    db: Session = Depends(deps.get_db),
    # current_user: Optional[models.User] = Depends(deps.get_current_active_user)
) -> Any:
    
    tables = crud.table.get_table(
        db,
        min_price=min_price,
        max_price=max_price,
        site=site,
        table_type=table_type
    )

    return tables
