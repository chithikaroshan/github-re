import pytest
from app.services.github_service import fetch_repository

@pytest.mark.asyncio
async def test_fetch_repository():
    data = await fetch_repository("octocat", "Hello-World")
    assert "name" in data
