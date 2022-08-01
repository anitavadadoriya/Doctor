from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from typing import Optional, TypeVar, Generic


T = TypeVar('T')

class DoctorSchema(BaseModel):

    name : Optional [str] = None
    username : Optional [str] = None 
    email : Optional [str] = None
    mobile : Optional [int] = None
    sector : Optional [str] = None
    location : Optional [str] = None
    address : Optional [str] = None
    qualification : Optional [str] = None
    fees : Optional [str] = None
    image : Optional [str] = None
    password : Optional [str] = None     
    
    class Config:
        orm_mode =True

class Requestdoctorschema(BaseModel):
    parameter: DoctorSchema = Field(...)

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)
