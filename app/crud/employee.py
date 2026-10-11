from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


# CREATE
async def create_employee(
    db: AsyncSession,
    employee_data: EmployeeCreate,
) -> Employee:
    employee = Employee(
        name=employee_data.name,
        email=employee_data.email,
        department=employee_data.department,
        salary=employee_data.salary,
    )

    db.add(employee)
    await db.commit()
    await db.refresh(employee)

    return employee


# READ ALL
async def get_employees(
    db: AsyncSession,
) -> list[Employee]:
    result = await db.execute(select(Employee))
    return list(result.scalars().all())


# READ ONE
async def get_employee(
    db: AsyncSession,
    employee_id: int,
) -> Employee | None:
    result = await db.execute(
        select(Employee).where(Employee.id == employee_id)
    )

    return result.scalar_one_or_none()


# UPDATE
async def update_employee(
    db: AsyncSession,
    employee: Employee,
    employee_data: EmployeeUpdate,
) -> Employee:
    update_data = employee_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        if value is None:
            raise ValueError(f"{field} cannot be null")

        setattr(employee, field, value)

    await db.commit()
    await db.refresh(employee)

    return employee


# DELETE
async def delete_employee(
    db: AsyncSession,
    employee: Employee,
) -> None:
    await db.delete(employee)
    await db.commit()