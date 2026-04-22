from fastapi import FastAPI
from app.presentation.masters.profile.v1.routers import router as master_profile_router
from app.presentation.masters.auth.v1.routers import router as master_auth_router
from app.presentation.beauty_services.v1.routers import router as beauty_services_router
# Create a FastAPI application instance
app = FastAPI()

app.include_router(master_profile_router)
app.include_router(master_auth_router)
app.include_router(beauty_services_router)

