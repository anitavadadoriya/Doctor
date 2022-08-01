from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body
from server.database import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session
from server.controller.doctor import CryptContext
import base64
import uuid

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


from server.controller.doctor import(
    get_doctor,
    add_doctor,
    update_doctor_data, 
    get_doctor_by_id
)

from server.model.schema import(
    Requestdoctorschema,
    Requestupdatedoctorschema,
    RequestDoctorlogin
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create_doctor(request: Requestdoctorschema, db: Session = Depends(get_db)):
    try:
        await add_doctor(db, doctordata = request.parameter)
        return {"status":"Ok","code":200,"message":"Doctor created successfully"}
    except Exception as e:
        return {"Message": e.args, "code" :500}

@router.get("/")
async def get_books( db: Session = Depends(get_db)):
    doctordata = get_doctor(db)
    return  {'status':"Ok",'code':"200",'message':"All data show Sucessfully",'msg':doctordata}


@router.put("/update/{doctorregistration_id}")
async def update_doctor_data_by_id( doctorregistration_id : int, request : Requestupdatedoctorschema,db: Session = Depends(get_db)):
    try:
        data = jsonable_encoder(request)
        update_doctor = update_doctor_data(db, doctorregistration_id , **data.get('parameter'))
        return  {'status':"Ok",'code':200,"Message": "Doctor profie updated successfully.", "Data": update_doctor}
    except Exception as e:
        return {"Message" : e.args , "code":500}


@router.get("/getdata/{doctorregistration_id}")
async def getby_id(doctorregistration_id: int, db: Session = Depends(get_db)):    
    usersdata = get_doctor_by_id(db, doctorregistration_id= doctorregistration_id)
    if usersdata is None:
        return {"Msg" : "No doctor registered"}
    return {"Message" : usersdata}


@router.delete("/delete/{doctorregistration_id}")
async def delete_doctor_data( doctorregistration_id : int, db: Session = Depends(get_db)):
    try: 
        # import pdb
        # pdb.set_trace()
        
        db.delete(get_doctor_by_id(db, doctorregistration_id= doctorregistration_id))
        db.commit()

        return {'status':"Ok",'code':"200",'message':"Doctor Data delete successfully"}
    except Exception as e:
        return {"Message" : e.args}
    
@router.post("/doctorlogin")
async def doctor_login( request: RequestDoctorlogin, db: Session = Depends(get_db)):
    try:
        data = jsonable_encoder(request)
        doctor =await doctor_login(db, data.get('parameter').get('email'))
        if pwd_context.verify(data.get('parameter').get('password'), doctor.password):
            return {"status":"Ok","code":200,"message":"Doctor login successfully", "msg":"Hiii"}
        else:
            return {"status":"Error","code":400,"message":"Invalid password", "msg": "fcrvghj"}
    except Exception as e:
        return {"status":"Error","code":500,"message": e.args}
    

    
