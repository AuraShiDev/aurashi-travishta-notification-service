from enum import Enum

class EventType(str, Enum):
    BOOKING_CONFIRMED = "BOOKING_CONFIRMED"
    PAYMENT_SUCCESS = "PAYMENT_SUCCESS"
    TRIP_STARTED = "TRIP_STARTED"

class NotificationProvider(str, Enum):
    SES = "SES"
    SENDGRID = "SENDGRID"
    TWILIO = "TWILIO"

class TemplateChannel(str, Enum):
    EMAIL = "EMAIL"
    SMS = "SMS"

class NotificationStatus(str, Enum):
    pending = "PENDING"
    sent = "SENT"
    failed = "FAILED"
    retrying="RETRYING"
