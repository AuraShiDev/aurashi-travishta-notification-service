from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field,Relationship
from sqlalchemy import Column, String, Integer, DateTime, UniqueConstraint, text


class NotificationRequest(SQLModel, table=True):
    __tablename__ = "notification_requests"
    id: UUID = Field(default_factory=uuid4,primary_key=True,index=True)
    event_type: str = Field(sa_column=Column(String(50), nullable=False))#BOOKING_CONFIRMED, PAYMENT_SUCCESS, TRIP_STARTED
    reference_id: UUID = Field(nullable=False,index=True)

    user_id: UUID = Field(default_factory=uuid4,nullable=False,index=True)
    channel: str = Field(sa_column=Column(String(20), nullable=False))
    status: str = Field(sa_column=Column(String(20),nullable=False,server_default=text("'PENDING'")))
    retry_count: int = Field(default=0,sa_column=Column(Integer, nullable=False, server_default="0"))
    scheduled_at: datetime = Field(sa_column=Column( DateTime(timezone=True),nullable=False,server_default=text("NOW()")))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True),nullable=False,server_default=text("NOW()")))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True),nullable=False,server_default=text("NOW()"),onupdate=datetime.utcnow))
    __table_args__ = (
        UniqueConstraint(
            "event_type",
            "reference_id",
            "channel",
            name="uq_event_reference_channel"
        ),
    )

    failures: list["NotificationFailure"] = Relationship(back_populates="notification")
