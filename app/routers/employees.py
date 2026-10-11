from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import employee as employee_crud
from app.database import get_db
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate,
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)


# CREATE EMPLOYEE
@router.post(
    "/",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_employee(
    employee_data: EmployeeCreate,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await employee_crud.create_employee(
            db, employee_data
        )
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An employee with this email already exists",
        )


# READ ALL EMPLOYEES
@router.get(
    "/",
    response_model=list[EmployeeResponse],
)
async def read_employees(
    db: AsyncSession = Depends(get_db),
):
    return await employee_crud.get_employees(db)


# READ ONE EMPLOYEE
@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
async def read_employee(
    employee_id: int,
    db: AsyncSession = Depends(get_db),
):
    employee = await employee_crud.get_employee(
        db, employee_id
    )

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )

    return employee


# UPDATE EMPLOYEE
@router.patch(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
async def update_employee(
    employee_id: int,
    employee_data: EmployeeUpdate,
    db: AsyncSession = Depends(get_db),
):
    employee = await employee_crud.get_employee(
        db, employee_id
    )

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )

    try:
        return await employee_crud.update_employee(
            db, employee, employee_data
        )
    except ValueError as exc:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        )
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An employee with this email already exists",
        )


# DELETE EMPLOYEE
@router.delete(
    "/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_employee(
    employee_id: int,
    db: AsyncSession = Depends(get_db),
):
    employee = await employee_crud.get_employee(
        db, employee_id
    )

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )

    await employee_crud.delete_employee(db, employee)
    return None