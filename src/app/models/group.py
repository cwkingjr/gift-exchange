from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .exchange import Exchange  # noqa: F401


class Group(Base):
    id = Column(Integer, primary_key=True, index=True)
    exchange_id = Column(Integer, ForeignKey("exchange.id"))

    name = Column(String(60))

    exchange = relationship("Exchange", backref="groups")
