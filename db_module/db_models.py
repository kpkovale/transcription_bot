from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Integer, String, ForeignKey, \
    Float, UniqueConstraint, BigInteger, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime, timedelta
from typing import List, Tuple
from typing_extensions import Annotated

from utils.bot_logger import logger
from db_module.database import DBSession, engine, IDUMixin

intpk = Annotated[int, mapped_column(primary_key=True)]

from sqlalchemy.orm import registry

reg = registry()


class Base(DeclarativeBase):
    registry = reg


class User(Base, IDUMixin):
    """
    An example model class for SQLAlchemy.ORM
    """
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    phone = mapped_column(String, nullable=False, unique=True)
    email = mapped_column(String)  # , nullable=False, unique=True
    enroll_date = mapped_column(DateTime, nullable=False, insert_default=func.now())
    active = mapped_column(Boolean, nullable=False, insert_default=True)

    def __init__(self, *args, **kwargs):
        """

        :param kwargs: name / phone / email / telegram_id / enroll_date (optional)

        """
        super().__init__()
        for key, val in kwargs.items():
            self.__setattr__(key, val)

    def __repr__(self):
        email = self.email if self.email else ""
        return f"{self.__class__.__name__} (id: {self.id}, " \
               f"User name: {self.name}, " \
               f"Phone number: {self.phone}, " \
               f"email: {email}, " \
               f"Registration date: {self.enroll_date}, " \
               f"Active: {self.active})"

    def __str__(self, admin: bool = False):
        email = str(self.email) if self.email else ""
        email = email.replace("_", "\_")
        str_res = f"*Пользователь*: {self.name} \n" \
                  f"*Номер телефона*: `{self.phone}` \n" \
                  f"*Логин*: u{self.phone} \n" \
                  f"*Email*: {email} \n" \
                  f"*Дата регистрации*: {self.enroll_date}\n"
        str_res = str_res + f"\n*Активный:* {self.active}" if admin else str_res
        return str_res


if __name__ == '__main__':
    Base.metadata.create_all(engine)
