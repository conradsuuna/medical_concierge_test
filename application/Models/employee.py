from .. import session, engine
from sqlalchemy import Column, Integer, String, Enum
# from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

import enum

class Role(enum.Enum):
    Admin = 'Admin'
    Editor = 'Editor'
    Viewer = 'Viewer'

class StaffStatus(enum.Enum):
    left = 'left'
    pending = 'pending'
    active = 'active'

class TimeStatus(enum.Enum):
    old = 'old'
    new = 'new'

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    staff_status = Column(Enum(StaffStatus))
    role = Column(Enum(Role),nullable=True)
    time_spent_status = Column(Enum(TimeStatus))
    # designation = relationship(Designation, backref="designation")

    def __repr__(self):
        return f'{self.name}'

    def save(self):
        session.add(self)
        session.commit()

    def to_json(self):
        json_obj = {}
        for column in self.__table__.columns:
            json_obj[column.name] = str(getattr(self, column.name))
        return json_obj

# Base.metadata.create_all(engine) #edit here
Employee.__table__.create(engine, checkfirst=True)