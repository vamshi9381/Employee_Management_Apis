from pydantic import BaseModel, ConfigDict, EmailStr, Field


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    department: str = Field(min_length=2, max_length=100)
    salary: float = Field(gt=0)


class EmployeeUpdate(BaseModel):
    name: str | None = Field(
        default=None, min_length=2, max_length=100
    )
    email: EmailStr | None = None
    department: str | None = Field(
        default=None, min_length=2, max_length=100
    )
    salary: float | None = Field(default=None, gt=0)
    is_active: bool | None = None


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str
    salary: float
    is_active: bool

    model_config = ConfigDict(from_attributes=True)