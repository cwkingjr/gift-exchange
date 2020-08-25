from typing import TYPE_CHECKING

from sqlalchemy import Column, Date, Integer

from app.db.base_class import Base


class Participant(Base):
    id = Column(Integer, primary_key=True, index=True)
    exchange_id = Column(Integer, nullable=False, index=True)
    reminding_participant_id = Column(Integer, nullable=False, index=True)
    reminded_participant_id = Column(Integer, nullable=False, index=True)
    created_at = Column(Date, nullable=False, index=True)