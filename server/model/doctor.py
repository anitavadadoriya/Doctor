from pickle import LONG


from server.database import Base
from sqlalchemy import Column,Integer,String

class Doctorregistration(Base):
    __tablename__ = 'doctorregistration'
    id  = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    username = Column(String)
    email = Column(String, unique=True)
    mobile = Column(String)
    sector = Column(String)
    location = Column(String)
    address = Column(String)
    qualification = Column(String)
    fees= Column(String)
    image = Column(String)
    password = Column(String)
