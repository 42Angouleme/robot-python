from typing import Optional

from sqlalchemy.engine import create
from pybot.module_webapp.app import db
from .image_model_preset import DrawingModel
from datetime import datetime

UserId = int
"""Type for the User ID"""


class UserBase:
    first_name: str
    last_name: str
    picture_path: str
    picture: bytes
    conversation_summary: str


class UserCreate(UserBase):
    pass


class UserPatch:
    first_name: Optional[str]
    last_name: Optional[str]
    picture: Optional[bytes]
    conversation_summary: Optional[str]


class UserResponse(UserBase):
    id: UserId
    created_at: datetime
    picture: dict


class User(db.Model):
    """User database model"""

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    conversation_summary = db.Column(db.String(500), nullable=True, default="")
    picture = db.Column(DrawingModel.as_mutable_json())
