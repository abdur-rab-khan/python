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

from pydantic import BaseModel, Field, PositiveInt, ValidationError


class User(BaseModel):
    id: int
    age: PositiveInt
    first_name: str = Field(gt=1, lt=2)  # Use to add rules on each field
    last_name: str = Field(gt=1, lt=2)


try:
    user_1 = User(id=1, age=-20, first_name="Abdur Rab", last_name="Khan")
    print(user_1.model_dump())  # Converts into python dict
    print(user_1.model_dump_json())  # Converts into python json
except ValidationError as err:
    print(f"Validation error happened: {err.errors()}")
