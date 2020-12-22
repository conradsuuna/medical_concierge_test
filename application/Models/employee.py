from sqlalchemy.ext.declarative import declarative_base
from .. import session

Base = declarative_base()
from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship

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
    role = Column(Enum(Role))
    time_spent_status = Column(Enum(TimeStatus))
    # designation = relationship(Designation, backref="designation")

    def __repr__(self):
        return f'{self.name}'

    def save(self):
        session.add(self)
        session.commit()
        