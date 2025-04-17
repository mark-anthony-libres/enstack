from pydantic import BaseModel, field_validator, ValidationInfo
from sqlalchemy import Column, Integer, String, Boolean
from database import Base
import re

class LoginClass(BaseModel):
    username: str
    password:str

    @field_validator('username')
    def validate_username(cls: type, v: str):
        lower_username = v.lower()
        if len(lower_username) < 4:
            raise ValueError('Username must be at least 4 letters')
        if not re.search(r'a.*b.*c', lower_username):
            raise ValueError('Username must contain letters "a", "b", and "c" are in that order')
        return v
    
    @field_validator('password')
    def validate_password(cls: type, v: str, values : ValidationInfo):
        username = values.data.get('username', "")

        if v != username[::-1]:
            raise ValueError('Password will be valid if it is equal to the reverse of the username')
        
        return v
    

class Letter(Base):
    __tablename__ = "letters"

    id = Column(Integer, primary_key=True, index=True)
    letter = Column(String, unique=True, nullable=False)
    value = Column(Integer, nullable=False)
    strokes = Column(Integer, nullable=False)
    vowel = Column(Boolean, nullable=False)


class LetterInput(BaseModel):
    letter: str
    value: int
    strokes: int
    vowel: bool

    @field_validator("strokes")
    def strokes_must_not_equal_value(cls: type, v: str, values : ValidationInfo):
        if "value" in values.data and v == values.data.get('value'):
            raise ValueError("strokes must not be equal to value")
        return v
    

