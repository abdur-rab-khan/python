## 1. Fast API Folder Structure

```md
project/
├── app/
│ ├── main.py # App starts here
│ ├── core/
│ │ ├── config.py # Settings from .env
│ │ └── security.py # Password and token code
│ ├── db/
│ │ └── session.py # Database connection
│ ├── users/ # One feature = one folder
│ │ ├── router.py # URLs (endpoints)
│ │ ├── models.py # Database tables
│ │ ├── schemas.py # Request and response shape
│ │ ├── repository.py # Only database queries
│ │ ├── service.py # Main logic
│ │ └── dependencies.py # Reusable checks (Depends)
│ └── products/ # Same files as users/
├── tests/
├── alembic/ # Database changes (migrations)
├── .env
├── requirements.txt
└── Dockerfile
```

## 2. Fast API Code Structure

### 1. `main.py`

- This is the starting file. It only joins everything together.
- It should not have any business logic.

```py
from fastapi import FastAPI
from app.users.router import router as users_router
from app.products.router import router as products_router

app = FastAPI(title="My App")

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(products_router, prefix="/products", tags=["Products"])
```

### 2. `core/config.py`

- Keeps all settings in one place.
- Reads values from the .env file.

```py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"


settings = Settings()
```

### 3. `db/sessions.py`

- Makes the database connection.
- Gives a database session to each request.

```py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 4. `users/models.py`

- Describes the database table.

```py
from sqlalchemy import Column, Integer, String
from app.db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
```

### 5. `users/schemas.py`

- Describes what data comes in and what data goes out.
- Password is not in the response, so it stays safe.

```py
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
```

### 6. `users/repository.py`

- Only database work. No rules, no HTTP errors.

```py
from sqlalchemy.orm import Session
from app.users.models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
```

### 7. `users/service.py`

- Has the real work: save, find, update, delete.
- Router calls this file, so the router stays small.

```py
from sqlalchemy.orm import Session
from app.users.models import User
from app.users.schemas import UserCreate


# Without using any repository
def create_user(db: Session, data: UserCreate):
    user = User(email=data.email, password=data.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# With using repository
class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, data):
        if self.repo.get_by_email(data.email):
            raise HTTPException(status_code=400, detail="Email already used")
        user = User(email=data.email, password=data.password)
        return self.repo.create(user)
```

### 8. `users/dependencies.py`

- Joins everything: database → repository → service.

```py
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.users.repository import UserRepository
from app.users.service import UserService


def get_user_service(db: Session = Depends(get_db)):
    return UserService(UserRepository(db))
```

### 9. `users/router.py`

- Has only the URLs.
- It takes the request, calls the service, and sends the response.

```py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.users import service
from app.users.schemas import UserCreate, UserResponse

router = APIRouter()


# Without using any repository
@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, data)


# With using repository
@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate, service: UserService = Depends(get_user_service)):
    return service.register(data)
```
