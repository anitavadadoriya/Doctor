
from sqlalchemy.orm import Session
from server.model.doctor import Doctorregistration
from server.model.schema import DoctorSchema,updateDoctorSchema


from passlib.context import CryptContext




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from server.utils.image_hendler import image_upload

def add_doctor(db: Session, doctordata : DoctorSchema ):
   
    doctor = Doctorregistration(name=doctordata.name, 
                                username=doctordata.username,
                                email = doctordata.email,
                                mobile = doctordata.mobile,
                                sector = doctordata.sector,
                                location = doctordata.location,
                                address = doctordata.address, 
                                qualification = doctordata.qualification,
                                fees = doctordata.fees, 
                                image= doctordata.image,
                                password =  pwd_context.hash(doctordata.password) )
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor

def get_doctor(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Doctorregistration).offset(skip).limit(limit).all()

def get_doctor_by_id(db: Session, d_id: int):
    return db.query(Doctorregistration).filter(Doctorregistration.id == d_id).first()

def update_doctor(db: Session, d_id: int, name: str, username: str,mobile=int,sector=str,location=str,address=str,qualification=str,fees=str,image=str):
   
    update_doctor = get_doctor_by_id(db=db, d_id=d_id)
   
    update_doctor.name = name,
    update_doctor.username = username,
    update_doctor.mobile = mobile,
    update_doctor.sector = sector,
    update_doctor.location = location,
    update_doctor.address = address,
    update_doctor.qualification = qualification,
    update_doctor.fees = fees,
    update_doctor.image = image,
    
    db.commit()
    db.refresh(update_doctor)
    return update_doctor

def remove_doctor(db: Session, d_id: int):
    delete_doctor = get_doctor_by_id(db=db, d_id=d_id)
    db.delete(delete_doctor)
    db.commit()


def get_doctor_by_email(db: Session, emails: str):
    return db.query(Doctorregistration).filter(Doctorregistration.email == emails).first()
