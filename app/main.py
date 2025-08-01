from fastapi import FastAPI 
from prometheus_fastapi_instrumentator import Instrumentator 
from app.api import routes_auth, routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app = FastAPI(title="Car Price Prediction API")

# Link middleware 
app.add_middleware(LoggingMiddleware)

# Link endpoints 
app.include_router(routes_auth.router, tags=["Auth"])
app.include_router(routes_predict.router, tags=["Prediction"])

# Monitoring using Prometheus 
Instrumentator().instrument(app).expose(app)

# Add Exception handlers 
register_exception_handlers(app)
