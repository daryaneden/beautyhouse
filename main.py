from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from handlers import routers

# Create a FastAPI application instance
app = FastAPI()

for router in routers:
    app.include_router(router)