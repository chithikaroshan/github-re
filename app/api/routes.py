from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Repository
from app.schemas.repository import RepoCreate, RepoResponse, RepoUpdate
from app.services.github_service import fetch_repository
from app.core.exceptions import RepositoryNotFoundException

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST
@router.post("/repositories", response_model=RepoResponse, status_code=201)
async def create_repository(data: RepoCreate, db: Session = Depends(get_db)):
    github_data = await fetch_repository(data.owner, data.repo_name)

    repo = Repository(
        name=github_data["name"],
        owner=github_data["owner"]["login"],
        stars=github_data["stargazers_count"],
        forks=github_data["forks_count"],
        language=github_data["language"],
        repo_url=github_data["html_url"],
    )

    db.add(repo)
    db.commit()
    db.refresh(repo)
    return repo

# GET
@router.get("/repositories/{repo_id}", response_model=RepoResponse)
def get_repository(repo_id: str, db: Session = Depends(get_db)):
    repo = db.query(Repository).filter(Repository.id == repo_id).first()
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")
    return repo

# PUT
@router.put("/repositories/{repo_id}", response_model=RepoResponse)
def update_repository(repo_id: str, data: RepoUpdate, db: Session = Depends(get_db)):
    repo = db.query(Repository).filter(Repository.id == repo_id).first()
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(repo, key, value)

    db.commit()
    db.refresh(repo)
    return repo

# DELETE
@router.delete("/repositories/{repo_id}", status_code=204)
def delete_repository(repo_id: str, db: Session = Depends(get_db)):
    repo = db.query(Repository).filter(Repository.id == repo_id).first()
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")

    db.delete(repo)
    db.commit()
