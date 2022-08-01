from fastapi import APIRouter, Response
from server.database import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session

from server.controller.doctor import(
    add_doctor,
)

from server.model.schema import(
    Requestdoctorschema
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
    add_doctor(db, doctordata = request.parameter)
    return {"status":"Ok","code":200,"message":"Doctor created successfully"}
