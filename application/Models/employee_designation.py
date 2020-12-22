from sqlalchemy.ext.declarative import declarative_base
from .. import session
from sqlalchemy.orm import relationship

Base = declarative_base()
from sqlalchemy import Column, Integer, String

class Designation(Base):
    __tablename__ = 'designation'

    id = Column(Integer, primary_key=True)
    # employee_id = Column(Integer, ForeignKey('employee.id'))
    # employee = relationship('Employee')
    employee_id = Column(Integer)
    designation_type = Column(String)

    def __repr__(self):
        return f'{self.designatio_type}'

    def save(self):
        session.add(self)
        session.commit()
        