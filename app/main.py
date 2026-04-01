from fastapi import FastAPI
from beauty_services.handlers import router as beautyservice_router
from masters.profile.handlers import router as master_profile_router
from masters.auth.handlers import router as master_auth_router

# Create a FastAPI application instance
app = FastAPI()
app.include_router(beautyservice_router)
app.include_router(master_profile_router)
app.include_router(master_auth_router)

# for router in routers:
#     app.include_router(router)