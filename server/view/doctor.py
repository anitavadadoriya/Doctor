
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter
from server.database import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from server.controller.doctor import(
    get_doctor,
    add_doctor,
    get_doctor,
    update_doctor,
    remove_doctor,
    get_doctor_by_email,
    get_doctor_by_id
    
)

from server.model.schema import(
    Requestdoctorschema,
    Requestupdatedoctorschema,
    RequestLoginDoctorSchema,
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
        add_doctor(db, doctordata = request.parameter)
        return {"status":"Ok","code":200,"message":"Doctor created successfully",'result':request.parameter}
    except Exception as e:
        return {"status":"Error","code":400,"message": e.args}

@router.get("/all_doctors")
async def get_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        all_data = get_doctor(db, skip, limit)
        return {"status":"Ok", "code":"200", "message":"Success fetch all data","result":all_data}
    except Exception as e:
        return {"status":"Error","code":400,"message": e.args}

@router.get("/doctors_get_by_id/{d_id}")
async def get_doctor_by_id_data(d_id: int , db: Session = Depends(get_db)):
    try:
        doctor_data = get_doctor_by_id(db, d_id)
        if doctor_data:
            return {"status":"Ok", "code":"200", "message":"Success fetch data","result":doctor_data}
        else:
            return {"status":"Error","code":400,"message":"No data found"}
      
    except Exception as e:
        return {"status":"Error","code":400,"message": e.args}


@router.put("/update/{d_id}")
async def update_doctor_data(d_id: int ,request: Requestupdatedoctorschema, db: Session = Depends(get_db)):
    # all_data_id = get_doctor_by_id(db,d_id)

    try:
        data = jsonable_encoder(request)
       
        updated_doctor = update_doctor(db, d_id, **data.get('parameter')) 
          
        return {"status":"Ok","code":200,"message":"Doctor updated successfully","result":updated_doctor}
    except Exception as e:
        return {"status":"Error","code":400,"message": e.args}
                             
@router.delete("/delete/{d_id}")
async def delete_doctor(request: Requestdoctorschema,  db: Session = Depends(get_db),d_id: int = 0,):
    try:
        remove_doctor(db, d_id)
        return {"status":"Ok","code":200,"message":"Doctor deleted successfully"}
    except Exception as e:
        return {"status":"Error","code":400,"message": e.args}
   
@router.post("/doctorlogin")
async def doctor_login( request: RequestLoginDoctorSchema, db: Session = Depends(get_db)):
    try:
        data = jsonable_encoder(request)
        doctor = get_doctor_by_email(db, data.get('parameter').get('email'))
        if pwd_context.verify(data.get('parameter').get('password'), doctor.password):
            return {"status":"Ok","code":200,"message":"Doctor login successfully"}
        else:
            return {"status":"Error","code":400,"message":"Invalid password"}
    except Exception as e:
        return {"status":"Error","code":400,"message": e.args}
    


        

    
