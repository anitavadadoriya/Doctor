from msilib.schema import File
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

class Doctordataupdate(BaseModel):
    
    name : Optional [str] = None
    username : Optional [str] = None 
    mobile : Optional [int] = None
    sector : Optional [str] = None
    location : Optional [str] = None
    address : Optional [str] = None
    qualification : Optional [str] = None
    fees : Optional [str] = None
    image : Optional [str] = None


class doctorlogin(BaseModel):
    
    email : Optional [str] = None
    password : Optional [str] = None

class Requestupdatedoctorschema(BaseModel):
    parameter: Doctordataupdate = Field(...)
     
    
class Requestdoctorschema(BaseModel):
    parameter: DoctorSchema = Field(...)

class RequestDoctorlogin(BaseModel):
    parameter : doctorlogin = Field (...)

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class updateDoctorSchema(BaseModel):
   
    name : Optional [str] = None
    username : Optional [str] = None 
    mobile : Optional [int] = None
    sector : Optional [str] = None
    location : Optional [str] = None
    address : Optional [str] = None
    qualification : Optional [str] = None
    fees : Optional [str] = None
    image : Optional [str] = None
      
    
    class Config:
        orm_mode =True

class Requestupdatedoctorschema(BaseModel):
    parameter: updateDoctorSchema = Field(...)

class LoginDoctorSchema(BaseModel):
   
    
    email : Optional [str] = None    
    password : Optional [str] = None
      
    
    class Config:
        orm_mode =True

class RequestLoginDoctorSchema(BaseModel):
    parameter: LoginDoctorSchema = Field(...)
