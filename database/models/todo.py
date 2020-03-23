from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    content = Column(String(200))
    status = Column(Integer)

    def __str__(self):
        return f"{self.id}. {self.content}"
