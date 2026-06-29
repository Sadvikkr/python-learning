from fastapi import FastAPI

from app.config import *
from app.routes.student import router

app = FastAPI()

app.include_router(router)










           

    
        

    