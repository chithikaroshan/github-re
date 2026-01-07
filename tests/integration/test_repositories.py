from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_repository():
    response = client.post(
        "/repositories",
        json={"owner": "octocat", "repo_name": "Hello-World"}
    )
    assert response.status_code == 201
