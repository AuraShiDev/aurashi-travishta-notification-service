from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, DateTime, Text, text


class NotificationFailure(SQLModel, table=True):
    __tablename__ = "notification_failures"
    id: UUID = Field(default_factory=uuid4,primary_key=True,index=True)
    notification_id: UUID = Field(foreign_key="notification_requests.id",nullable=False,index=True)
    error_message: str = Field(sa_column=Column(Text, nullable=False))
    failed_at: datetime = Field(sa_column=Column(DateTime(timezone=True),nullable=False,server_default=text("NOW()")))

    notification: Optional["NotificationRequest"] = Relationship(back_populates="failures")
