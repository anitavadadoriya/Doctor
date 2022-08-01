from sqlalchemy.orm import Session
from server.model.doctor import Doctorregistration
from server.model.schema import DoctorSchema


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
                                password = doctordata.password )
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor


