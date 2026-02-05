from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, Boolean, DateTime, Text, UniqueConstraint, text


class NotificationTemplate(SQLModel, table=True):
    __tablename__ = "notification_templates"
    id: UUID = Field(default_factory=uuid4,primary_key=True,index=True)
    template_code: str = Field(sa_column=Column(String(50), nullable=False))#BOOKING_CONFIRM_EMAIL
    channel: str = Field(sa_column=Column(String(20), nullable=False))#EMAIL, SMS
    subject_template: Optional[str] = Field(sa_column=Column(Text, nullable=True))
    body_template: Optional[str] = Field(sa_column=Column(Text, nullable=True))
    is_active: bool = Field(sa_column=Column(Boolean,nullable=False,server_default=text("true")))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True),nullable=False,server_default=text("NOW()")))
    __table_args__ = (
        UniqueConstraint(
            "template_code",
            "channel",
            name="uq_template_code_channel"
        ),
    )
