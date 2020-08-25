from typing import TYPE_CHECKING

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .series import Series  # noqa: F401
    from .user import User  # noqa: F401


class Exchange(Base):
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    series_id = Column(Integer, ForeignKey("series.id"))

    desired_lock_date = Column(Date)
    gift_max_dollars = Column(Integer)
    name = Column(String(50))

    owner = relationship("User", backref="exchanges")
    series = relationship("Series", backref="exchanges")