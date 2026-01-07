from pydantic import BaseModel, HttpUrl, constr
from uuid import UUID
from typing import Optional

# Model to create a repo
class RepoCreate(BaseModel):
    owner: constr(min_length=1, strip_whitespace=True)
    repo_name: constr(min_length=1, strip_whitespace=True)

# Model to update a repo
class RepoUpdate(BaseModel):
    stars: Optional[int] = None
    forks: Optional[int] = None
    language: Optional[str] = None

# Model for response
class RepoResponse(BaseModel):
    id: UUID
    name: str
    owner: str
    stars: int
    forks: int
    language: Optional[str] = None
    repo_url: HttpUrl

    class Config:
        orm_mode = True

