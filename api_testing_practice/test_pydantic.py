from enum import Enum
from typing import List

from api_testing_practice.utils.data_generator import DataGenerator
from pydantic import BaseModel, Field


'''class User(BaseModel):
    email: str
    fullName: str
    password: str
    passwordRepeat: str
    roles: List[str]


def user_data():
    return DataGenerator.generate_user_data()


def test_user_pydantic():
    user = User(**user_data())
    assert user.password == '12345678Aa'
    print(user.password)
    print("Тест пройден успешно!")

class ProductType(str, Enum):
    NEW = 'NEW'
    OLD = 'OLD'


class Base(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)#длина имени должна быть от 3 до 50 символов 
    price: float = Field(default=0.0, ge=0, le=1000, description='price coat') #от 0 до 1000, по умолчанию стоит 0
    product: ProductType

def test_product():
    product = Base(name='ZXC', price=99.0, product=ProductType.NEW)
    print(product)'''


class Type(Enum):
    ELECTRIC = 'electric'
    CLOTH = 'cloth'


class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = Field(default=False)
    product_type: Type


def test_product_serialization():
    product = Product(name='Adidas', price=10.0, product_type=Type.CLOTH)

    json_data = product.model_dump_json()
    print(f"Serialized: {json_data}")

    new_user = product.model_validate_json(json_data)
    print(new_user.name)























