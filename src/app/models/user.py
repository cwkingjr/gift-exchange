from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(80), unique=True, index=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    name = Column(String(60), index=True, nullable=False)
    password_salt = Column(String(50), nullable=False)


def get_test_user():
    return User(
        id=1,
        email="test@example.com",
        hashed_password="A5B4C2",
        name="test user",
        password_salt="mysalt"
    )
