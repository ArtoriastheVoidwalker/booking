from typing import Optional, List
from pydantic import BaseModel
from app.models.table import TableStatus, TableType


class TableBase(BaseModel):
    site: int
    price: int
    table_status: TableStatus
    table_type: TableType


class TableCreate(BaseModel):
    site: int
    price: int
    table_status: TableStatus = 'is_free'
    table_type: TableType


class TableUpdate(BaseModel):
    site: int
    price: int
    table_status: TableStatus
    table_type: TableType



class TableInDBBase(TableBase):
    id: Optional[int]

    class Config:
        orm_mode = True


class Table(TableInDBBase):
    pass


class Tables(BaseModel):
    tables: List[Table] = []
    amount: Optional[int]
