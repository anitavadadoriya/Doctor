from fastapi import FastAPI
from .view.doctor import router as DoctorRouter
import server.model.doctor 
from server.database import Base,engine

server.model.doctor.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(DoctorRouter, tags=["Doctor"], prefix="/Doctor")



@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this Patient registration app!"}