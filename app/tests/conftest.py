# app/tests/conftest.py
from typing import AsyncGenerator
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.middleware.AuthMiddeware import get_current_user, get_admin_user


MOCK_ADMIN = {"user_id": "admin123", "role_id": 1, "username": "admin", "email": "admin@example.com"}


@pytest.fixture()
async def async_client() -> AsyncGenerator:
    # Override the dependency at the app level — bypasses the whole chain
    app.dependency_overrides[get_current_user] = lambda: MOCK_ADMIN
    app.dependency_overrides[get_admin_user] = lambda: MOCK_ADMIN

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        yield ac

    app.dependency_overrides.clear()  # clean up after each test