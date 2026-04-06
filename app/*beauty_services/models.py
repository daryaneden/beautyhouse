from app.infrastructure.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class BeautyServices(Base):
    __tablename__ = "BeautyServices"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    service_name: Mapped[str] = mapped_column(nullable=False)
    client_name: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[str] = mapped_column(nullable=False)
    master_id: Mapped[int] = mapped_column(ForeignKey("Masters.id"), nullable=False)