from typing import List

from pydantic import BaseModel, Field


class Attachment(BaseModel):
    attach: str
    editing: str
    fileName: str
    fileSize: str
    filecontent: str
    principal: str


class ItemAttachments(BaseModel):
    attachmentSequence: int
    attachments: Attachment
    colleagueId: str
    colleagueName: str
    companyId: str
    deleted: str
    description: str
    documentType: str
    newAttach: str
    processInstanceId: int
    size: str


class Attachments(BaseModel):
    item: List[ItemAttachments] = Field(default_factory=list)


class Colleagues(BaseModel):
    item: str


class Item(BaseModel):
    key: str
    value: str


class CardData(BaseModel):
    item: List[Item] = Field(default_factory=list)
