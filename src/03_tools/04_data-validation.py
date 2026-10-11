# PYDANTIC -- Data Validation
"""
🟡 1. What is Pydantic

    ⭕ Pydantic checks data while the code runs. It uses your type hints as the rules.
       Data from outside (user input, API, files, env variables) can be wrong.
       Pydantic gives a clear error if it is wrong.

        1. uv add pydantic                          [Install Pydantic (use version 2)]
        2. uv add "pydantic[email]"                 [Also install email checking]
        3. uv add pydantic-settings                 [For reading settings from .env]

🟡 2. Basic Model

    ⭕ Example:
        from pydantic import BaseModel, Field

        class User(BaseModel):
            name: str
            age: int = Field(ge=0, le=120)          [age must be 0 to 120]
            email: str | None = None

        user = User(name="Ali", age="25")           [Text "25" is changed to number 25]

    ⭕ Important Commands:
        1. User(**data)                             [Create and validate from a dict]
        2. User.model_validate(data)                [Validate a dict]
        3. User.model_validate_json(text)           [Validate a JSON string]
        4. user.model_dump()                        [Convert to a dict]
        5. user.model_dump_json()                   [Convert to a JSON string]

🟡 3. Field Rules

    1. Field(min_length=3, max_length=20)           [Length rules for text]
    2. Field(gt=0)                                  [Greater than 0]
    3. Field(ge=0, le=100)                          [From 0 to 100]
    4. Field(pattern=r"^\d{10}$")                   [Match a text pattern]
    5. Field(default_factory=list)                  [Safe default for lists or dicts]

🟡 4. Custom Checks

    1. @field_validator("name")                     [Check one field]
    2. @model_validator(mode="after")               [Check many fields together]

    ⭕ Example:
        from pydantic import field_validator

        class User(BaseModel):
            name: str

            @field_validator("name")
            @classmethod
            def name_not_empty(cls, v: str) -> str:
                if not v.strip():
                    raise ValueError("name cannot be empty")
                return v

🟡 5. Handling Errors

    ⭕ Example:
        from pydantic import ValidationError

        try:
            User(name="Ali", age=-5)
        except ValidationError as e:
            print(e.errors())                       [Shows which field failed and why]

🟡 6. Settings for a Model

    1. ConfigDict(strict=True)                      [No auto change, "25" will be an error for int]
    2. ConfigDict(extra="forbid")                   [Error if unknown fields are sent]
    3. ConfigDict(frozen=True)                      [Object cannot be changed after creation]
    4. TypeAdapter(list[int]).validate_python(x)    [Validate without making a model class]

    ⭕ Example:
        from pydantic import BaseModel, ConfigDict

        class User(BaseModel):
            model_config = ConfigDict(strict=True, extra="forbid")
            name: str

🟡 7. Reading Settings from .env

    ⭕ Example:
        from pydantic_settings import BaseSettings

        class Settings(BaseSettings):
            database_url: str
            debug: bool = False

        settings = Settings()                       [Reads from env variables and .env file]

🟡 8. Important Concepts

    1. Never trust outside data. Validate it where it enters your code.
    2. Pydantic changes types by default ("25" becomes 25). Use strict mode to stop this.
    3. Use extra="forbid" to catch spelling mistakes in field names.
    4. Use Field(...) rules instead of writing many if checks by hand.
    5. Use pydantic-settings for config, so wrong settings fail at start, not later.
    6. Validate once at the edge, then trust the model inside your code.
    7. Type checkers check code before it runs. Pydantic checks real data while it runs. Use both.
"""

from typing import Annotated, Literal

from bcrypt import gensalt, hashpw
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PositiveInt,
    ValidationError,
    field_validator,
    model_validator,
)
from pydantic_settings import BaseSettings


# 🟡 BaseSettings, extract the environment variables from ".env" file with and put the validation as well
class Settings(BaseSettings):
    debug: bool
    secret_key: str
    database_url: str

    model_config = {"env_file": ".env.example"}


try:
    env = Settings()
    print(f"Environment Variables are: {env.model_dump()}")
except ValidationError as err:
    print(f"Failed to get required settings: {err.errors()}")

# def check_and_hash(v: str) -> str:
#     if len(v) < 8:
#         raise ValueError("Password must be at least 8 characters long")
#     return hashpw(v.encode(), gensalt()).decode()


# HashedPassword = Annotated[str, AfterValidator(check_and_hash)]


# 🟡 Providing data to user class does two things:
#       1. parsing
#       2. validating
class User(BaseModel):
    id: int
    age: PositiveInt
    username: str
    password: str
    confirm_password: Annotated[str, Field(exclude=True)]

    # 👉 Field function is used to attach constraints on the field, like "first_name" must be greater than 1 and less than 255
    first_name: str = Field(
        min_length=1, max_length=255, description="Name of the User"
    )  # Use to add rules on each field
    last_name: str = Field(min_length=1, max_length=255)

    # 👉 Annotated is another way to make type in pydentic
    address: Annotated[str, Field(min_length=10, max_length=255)]

    # 👉 Field with default value
    # version: float = 3.15
    version: Annotated[float, Field(default=3.15)]

    # 👉 Literal allow to add literal value
    role: Literal["admin", "user"] = Field(
        default="admin",
        validate_default=True,
        description="Metadata about the field mostly google in AI to provide metadata",
    )

    # 👉 Pydantic also allow to add custom "field_validator" as well as "model_validator"
    #   1. "field_validator" adds validation on a particular field with custom validation
    #   2. "model_validator" allows to add validation on many fields together
    @field_validator("username")
    @classmethod
    def no_spaces(cls, v):
        if " " in v:
            raise ValueError("Username cannot have spaces")
        return v.lower()

    # 👉 "model_validator" allows to add validation on many fields together and also we can provide model that tell pydantics to run custom validator either after or before pydantic has checked it's must because sometime we add typecasting.
    @model_validator(mode="after")
    def check_password(self):
        if self.password != self.confirm_password:
            raise ValueError("Password do not match")
        self.password = hashpw(self.password.encode(), gensalt()).decode()
        return self

    # It allows to modify the configuration like by default "pydentic" does not allow extra fields
    model_config = ConfigDict(extra="allow")


try:
    user_1 = User(
        id=1,
        age=20,
        version=3.15,
        role="admin",
        # password="python111",
        password="python123",
        confirm_password="python123",
        username="Python",
        first_name="Python",
        last_name="Google",
        address="United State",
    )

    # 👉 Converting the provided data into "python dict", "json"
    print(user_1.model_dump())
    print(user_1.model_dump_json())

    # 👉 Just validating the data, from "dict", "json" and returns the User class
    dict_user = User.model_validate(
        {
            "id": 1,
            "age": 21,
            "username": "Python",
            "role": "admin",
            "password": "python123",
            "confirm_password": "python123",
            "first_name": "Python",
            "last_name": "Google",
            "address": "United State",
        }
    )
    json_user = User.model_validate_json(
        '{"id": 1, "age": 21, "username": "Python", "role": "admin", "password": "python123", "confirm_password": "python123", "first_name": "Python", "last_name": "Google", "address": "United State"}'
    )
except ValidationError as err:
    print(f"Validation error happened: {err.errors()}")
