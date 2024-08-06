from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.self import router as self_router
from app.routes.secure import router as secure_router

class FastAPIApp:
    def __init__(self):
        self.app = FastAPI()
        self._include_routes()

    def _include_routes(self):
        self.app.include_router(health_router)
        self.app.include_router(self_router)
        # self.app.include_router(secure_router)

    def get_app(self):
        return self.app

fastapi_app = FastAPIApp()
app = fastapi_app.get_app()
