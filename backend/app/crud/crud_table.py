from typing import Optional, Union, Dict, Any, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models import Table
from app.schemas import TableCreate, TableUpdate


class CRUDTable(CRUDBase[Table, TableCreate, TableUpdate]):  

    def get_table(
        self,
        db: Session, *, 
        min_price: int,
        max_price: int,
        site: int,
        table_type: str,
        skip: int = 0,
        limit: int = 100
    ) -> Any:

        tables = (
            db
            .query(Table)
            .order_by(Table.price)
            .filter((Table.table_type == table_type) &
                    (Table.site == site) & 
                    (Table.price >= min_price) &
                    (Table.price <= max_price))
            .offset(skip)
            .limit(limit)
            .all()
        )
        amount = len(tables)
        return {'tables': tables, 'amount': amount}

    def create(self, db: Session, *, obj_in: TableCreate) -> Table:

        db_obj = Table(
            site=obj_in.site,
            price=obj_in.price,
            table_status=obj_in.table_status,
            table_type=obj_in.table_type
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, id: int, obj_in: Union[TableUpdate, Dict[str, Any]]
    ) -> Table:

        db_obj = self.get(db, id=id)

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


table = CRUDTable(Table)
