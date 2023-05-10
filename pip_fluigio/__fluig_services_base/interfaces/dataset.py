from typing import List, Optional

from pydantic import BaseModel, Field


class StructConstraint(BaseModel):
    constraint_type: Optional[str]
    field_name: Optional[str]
    init_value: Optional[str]
    final_value: Optional[str]
    like_search: Optional[str] = ""


class Constraints(BaseModel):
    constraint: List[StructConstraint] = Field(default_factory=list)


class StructField(BaseModel):
    item: Optional[str]


class StructOrder(BaseModel):
    item: Optional[str]


class DatasetPurgeParams(BaseModel):
    company_id: Optional[str]
    user_name: Optional[str]
    password: Optional[str]
    dataset_name: Optional[str]


class DatasetQuery(BaseModel):
    company_id: Optional[str]
    user_name: Optional[str]
    password: Optional[str]
    dataset_name: Optional[str]
    fields: List[StructField] = Field(default_factory=list)
    constraints: List[StructConstraint] = Field(default_factory=list)
    order: List[StructOrder] = Field(default_factory=list)


class DatasetQueryParams(BaseModel):
    field_name: Optional[str]
    value: Optional[str]
    type: str
