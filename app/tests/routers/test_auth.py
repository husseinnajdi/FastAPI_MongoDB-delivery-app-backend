from urllib import response

from httpx import AsyncClient
import pytest


@pytest.mark.asyncio
async def test_login(async_client: AsyncClient):
    response=await async_client.post("/auth/login",data={
        "username": "husseinnajdi32@gmail.com",
        "password": "12345"
    })
    print(response.json())
    assert response.status_code ==200


@pytest.mark.asyncio
async  def test_register(async_client: AsyncClient):
    response=await async_client.post("auth/register",json={
        "username":"testuser",
        "email":"test@gmail.com",
        "password":"1234",
        "phone":"123456",
        "role_id": 1
    })
    print(response.json())
    assert response.status_code ==200

