from sqlalchemy.orm import Session
from server.model.doctor import Doctorregistration
from server.model.schema import DoctorSchema
from passlib.context import CryptContext

from server.utils.image_hendler import image_upload

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_doctor(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Doctorregistration).offset(skip).limit(limit).all()

def get_doctor_by_id(db: Session, doctorregistration_id: int):
    return db.query(Doctorregistration).filter(Doctorregistration.id == doctorregistration_id).first()

async def add_doctor(db: Session, doctordata : DoctorSchema ):

    
    img_path=await image_upload(doctordata.image)
    
    doctor = Doctorregistration(name=doctordata.name, 
                                username=doctordata.username,
                                email = doctordata.email,
                                mobile = doctordata.mobile,
                                sector = doctordata.sector,
                                location = doctordata.location,
                                address = doctordata.address, 
                                qualification = doctordata.qualification,
                                fees = doctordata.fees, 
                                image= img_path,
                                password =  pwd_context.hash(doctordata.password))
    db.add(doctor)  
    db.commit()
    db.refresh(doctor)
    return doctor


def update_doctor_data(db: Session, doctorregistration_id : int,name: str, username : str, email : str, mobile : int, sector : str, location : str ,
                       address :str, qualification : str,fees : str, image: str):
    doctor = get_doctor_by_id(db=db, doctorregistration_id=doctorregistration_id)
    
    doctor.name=name 
    doctor.username=username,
    doctor.email = email,
    doctor.mobile = mobile,
    doctor.sector = sector,
    doctor.location = location,
    doctor.address = address, 
    doctor.qualification = qualification,
    doctor.fees = fees, 
    doctor.image= image,

    db.commit()
    db.refresh(doctor)
    return doctor

def doctor_login(db: Session, loginemail:str ):
    return db.query(Doctorregistration).filter(Doctorregistration.email == loginemail).first()