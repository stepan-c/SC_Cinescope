from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, List
from api_testing_practice.utils.roles import Roles


class TestUser(BaseModel):
    email: str
    fullName: str
    password: str
    passwordRepeat:str = Field(..., min_length=3,max_length=20)
    roles: List[Roles] = [Roles.USER]
    verified: Optional[bool] = None
    banned: Optional[bool] = None

    model_config = ConfigDict(
        use_enum_values=True,  # автоматическое преобразование enum в значения
        json_encoders={
            Roles: lambda v: v.value
        }
    )

    @field_validator("passwordRepeat")
    def check_password_repeat(cls, value: str, info) -> str:
        if "password" in info.data and value != info.data["password"]:
            raise ValueError("Пароли не совпадают")
        return value


class RegisterUserResponse(BaseModel):
    id: str
    email: str = Field(pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", description="Email пользователя")
    fullName: str = Field(min_length=1, max_length=100, description="Полное имя пользователя")
    verified: bool
    banned: bool
    roles: List[Roles]
    createdAt: str

    model_config = ConfigDict(use_enum_values=True)

