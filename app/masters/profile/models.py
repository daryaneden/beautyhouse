from app.infrastructure.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

class Masters(Base):
    __tablename__ = "Masters"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    full_name: Mapped[Optional[str]] = mapped_column(nullable=True)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[Optional[str]]