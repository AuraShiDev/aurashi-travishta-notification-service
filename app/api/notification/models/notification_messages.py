from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String, DateTime, Text, ForeignKey


class NotificationMessage(SQLModel, table=True):
    __tablename__ = "notification_messages"

    id: UUID = Field(default_factory=uuid4,primary_key=True,index=True)
    notification_id: UUID = Field(foreign_key="notification_requests.id",nullable=False,index=True)
    recipient: str = Field(sa_column=Column(String(150), nullable=False))
    subject: Optional[str] = Field(sa_column=Column(String(200), nullable=True))
    body: Optional[str] = Field(sa_column=Column(Text, nullable=True))
    provider: str = Field(sa_column=Column(String(50), nullable=False))#SES, SENDGRID, TWILIO
    provider_message_id: Optional[str] = Field(sa_column=Column(String(150), nullable=True))
    sent_at: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), nullable=True))

    # MANY messages → ONE request
    notification: Optional["NotificationRequest"] = Relationship(
        back_populates="messages"
    )
