from .. import session, engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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

    def to_json(self):
        json_obj = {}
        for column in self.__table__.columns:
            json_obj[column.name] = str(getattr(self, column.name))
        return json_obj

# Base.metadata.create_all(engine) #edit here
Designation.__table__.create(engine, checkfirst=True)