from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exception_handlers import RequestValidationError
from fastapi.responses import JSONResponse
from src.api.endpoints.products import router as products_router
from src.api.endpoints.sales import router as sales_router
from src.api.endpoints.users import router as users_router
from src.api.endpoints.inventory import router as inventory_router
from src.api.endpoints.reports import router as reports_router
from src.api.endpoints.invoices import router as invoices_router
from src.api.endpoints.notifications import router as notifications_router
from src.api.endpoints.auth import router as auth_router
from src.utils.error_handler import global_exception_handler

app = FastAPI()

app.include_router(products_router)
app.include_router(sales_router)
app.include_router(users_router)
app.include_router(inventory_router)
app.include_router(reports_router)
app.include_router(invoices_router)
app.include_router(notifications_router)
app.include_router(auth_router)

# CORS (optional, for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global error handler
app.add_exception_handler(Exception, global_exception_handler)

@app.get("/")
def read_root():
    return {"message": "SENA_TEST backend is running!"}
