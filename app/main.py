from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app.models.employee import Employee  # Register the model
from app.routers.employees import router as employee_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables that do not exist yet.
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield

    # Dispose of database connections on shutdown.
    await engine.dispose()


app = FastAPI(
    title="Employee Management API",
    description=(
        "A REST API for managing employee records "
        "using FastAPI, PostgreSQL, and SQLAlchemy ORM."
    ),
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/", tags=["Health"])
async def root():
    return {
        "message": "Employee Management API is running"
    }


app.include_router(employee_router)