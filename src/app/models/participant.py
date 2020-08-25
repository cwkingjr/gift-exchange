from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .exchange import Exchange  # noqa: F401
    from .group import Group  # noqa: F401


class Participant(Base):
    id = Column(Integer, primary_key=True, index=True)
    exchange_id = Column(Integer, ForeignKey("exchange.id"))
    group_id = Column(Integer, ForeignKey("group.id"))
    
    email = Column(String(80), nullable=False)
    name = Column(String(60), nullable=False)
    token = Column(String(250), nullable=False)

    # filled in by participant
    submitted_theme = Column(String(80))

    # assigned by cycle code
    gift_for_participant_id = Column(Integer)
    use_theme_of_participant_id = Column(Integer)

    exchange = relationship("Exchange", backref="participants")
    group = relationship("Group", backref="participants")