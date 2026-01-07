import httpx
from app.core.exceptions import ExternalServiceUnavailableException

async def fetch_repository(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except Exception:
        raise ExternalServiceUnavailableException("GitHub API unavailable")
