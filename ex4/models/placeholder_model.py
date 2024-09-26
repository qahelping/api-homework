from pydantic import (BaseModel, Field,
                      AnyHttpUrl, EmailStr)
from typing import Optional


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class Geo(BaseModel):
    lat: Optional[float] = Field(None, ge=-90, le=90)
    lng: Optional[float] = Field(None, ge=-180, le=180)


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class User(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    phone: str
    website: str
    company: Company
    address: Address


class Todos(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool


class Photos(BaseModel):
    albumId: int
    id: int
    title: str
    url: AnyHttpUrl
    thumbnailUrl: AnyHttpUrl


class Albums(BaseModel):
    userId: int
    id: int
    title: str


class Comments(BaseModel):
    postId: int
    id: int
    name: str
    email: EmailStr
    body: str


class Posts(BaseModel):
    userId: int
    id: int
    title: str
    body: str

