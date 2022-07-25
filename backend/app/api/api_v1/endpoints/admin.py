from typing import Any
from datetime import datetime as datatime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps


router = APIRouter()


@router.post("/admin/table", response_model=schemas.Table)
async def create_table(
    *,
    db: Session = Depends(deps.get_db),
    table_data: schemas.TableCreate,
    # current_moderator: models.Moderator = Depends(deps.get_current_active_admin)
) -> Any:
    return crud.table.create(db, obj_in=table_data)


@router.patch("/admin/table/{id}", response_model=schemas.Table)
async def update(
    *,
    id: int,
    table_data: schemas.TableUpdate,
    db: Session = Depends(deps.get_db),
    # current_moderator: models.Moderator = Depends(deps.get_current_active_admin)
):
    if crud.table.get(db, id=id) is None:
        raise HTTPException(status_code=404, detail="Table not found")

    if str(table_data.table_status) == 'TableStatus.is_free':
        booking = crud.booking.get_by_table(db=db, table_id=id)
        crud.booking.update(db, booking_id=booking.id, obj_in={"status":"reject"})

    return crud.table.update(db, id=id, obj_in=table_data)


@router.patch("/admin/booking/accepted/{id}", response_model=schemas.Booking)
async def accepted(
    *,
    id: int,
    db: Session = Depends(deps.get_db),
    # current_moderator: models.Moderator = Depends(deps.get_current_active_admin)
):
    booking = crud.booking.get(db, id=id)

    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    table = crud.table.get(db=db, id=booking.table_id)
    crud.table.update(db=db, id=table.id, obj_in={"table_status":"booked"})

    return crud.booking.update(db, booking_id=id, obj_in={"status":"accepted"})


@router.patch("/admin/booking/reject/{id}", response_model=schemas.Booking)
async def reject(
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

    return crud.booking.update(db, booking_id=id, obj_in={"status":"reject"})


@router.delete("/admin/table/{id}")
async def delete(
    id: int,
    db: Session = Depends(deps.get_db),
    # current_moderator: models.Moderator = Depends(deps.get_current_active_admin),
):
    if crud.table.get(db, id=id) is not None:
        crud.table.remove(db, id=id)
    else:
        return HTTPException(status_code=404, detail="Table not found")
