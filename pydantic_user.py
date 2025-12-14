from pydantic import BaseModel




class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True

invalid_user_data = {
    "id": "one",
    "username": "test",
    "email": "email@gmail.com",
}

invalid_user = User(**invalid_user_data)