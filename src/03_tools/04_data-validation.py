from typing import Annotated, Any, Self
from uuid import uuid4

from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    computed_field,
    field_serializer,
    field_validator,
    model_serializer,
    model_validator,
)
from pydantic_settings import BaseSettings

# <-------------------------------------> 🟡 MODEL and FIELDS <------------------------------------->
# 🟡 Model in Pydantic use to define schema of an object along with validation logic and serializing logic
# 🟡 To make schema we use """BaseModel""" class, it does few things automatically type """data conversion""", """type casting""" like converting "float -> int", "string -> number"
# 🟡 To disable performing """type conversion""", we can enable """strict""" model that force pydantic to reject any data that does not match to the schema.
# 🟡 By default pydantic allow the add of """extra fields""" but using """extra=forbid""" we can reject that


# 🟡 Field in Pydantic use to configure, constrain, and metadata to individual attribute inside the pydantic model, using "Field" method.
# 🟡 To apply field we can either directly specify like this "field_name: type = Field()", or using "Annotated[type, Field(), ...other_stuff(e.g, AfterValidation())]"
# 🟡 Field alias, allows different variable names like """validationAlias (getting camelCase from frontend)""", """serializationAlias (after serializing converting them into python snake_case)"""
# 🟡 """@computed_field""" allows to create dynamic field by using existing fields
class APIRequest(BaseModel):
    # "default_factory" use to create dynamic default value unlike just """default"""
    id: str = Field(default_factory=lambda: uuid4().hex)
    confidence: float
    limit: Annotated[int, Field(gt=0, le=100)]
    raw_payload: str = Field(
        min_length=1, max_length=255, description="Raw binary payload data"
    )

    @computed_field
    def limit_confidence(self) -> str:
        return str(self.limit) + "-" + str(self.confidence)

    # 👉 Use to configure the current model
    # model_config = ConfigDict(strict=True, extra="forbid")


try:
    api_request = APIRequest(limit="50", confidence="0.8", raw_payload="binary data")
    print("API Request data is: ", api_request.model_dump())

    api_request_payload = {"limit": 50, "confidence": 0.8, "raw_payload": "binary data"}
    api_request_dict = APIRequest.model_validate(api_request_payload)
    print("API Request data without directly: ", api_request_dict.model_dump())

    print(end="\n\n")
except ValidationError as err:
    print(f"Error on Model is: {err.errors()}")


# <-------------------------------------> 🟡 VALIDATOR <------------------------------------->
# 🟡 Validator in Pydantic allows to sanitize, transform, validate individual or whole model before or after pydantic process them.
# 🟡 These are usually run either before/after pydantic internal parsing/validation handles raw, dirty input

# def check_and_hash(v: str) -> str:
#     if len(v) < 8:
#         raise ValueError("Password must be at least 8 characters long")
#     return hashpw(v.encode(), gensalt()).decode()


# HashedPassword = Annotated[str, AfterValidator(check_and_hash)]


class ToolCallInput(BaseModel):
    tags: list[str]
    temperature: float

    # Use to run before pydantic own internal parsing/validation
    @field_validator("tags", mode="before")
    @classmethod
    def ensure_list(cls, v: Any):
        if isinstance(v, str):
            return [tag.strip() for tag in v.split(",")]
        return v

    # Use to run after pydantic own interval parsing means the data will be safe
    @field_validator("temperature", mode="after")
    @classmethod
    def check_range(cls, v: float) -> float:
        if not (0.0 <= v <= 2.0):
            raise ValueError("Temperature must be between 0.0 to 2.0")
        return v


class UserRegistration(BaseModel):
    password: str = Field(pattern="^[A-Za-z0-9]{6}$")
    confirm_password: str = Field(pattern="^[A-Za-z0-9]{6}$", exclude=True)

    # Use to run validation on the whole model data
    @model_validator(mode="after")
    def password_match(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError("Password do not match")
        return self

    # Use to run wrap the entire validation pipeline, allowing to custom exception handling or dynamic fallback
    @model_validator(mode="wrap")
    @classmethod
    def handle_validation_errors(cls, data: Any, handler) -> Any:
        try:
            return handler(data)
        except ValidationError as err:
            print(f"Failed to parse user data: {err}")
            raise err


try:
    tool_input = ToolCallInput(tags="Python, Fast-API, AI, LangChain", temperature=1.0)
    print(f"Tool Call is: {tool_input.model_dump()}")

    user_form = UserRegistration(password="kX7mP4", confirm_password="kX7mP4")
    print(f"Form Data is: {user_form.model_dump()}")

    print(end="\n\n")
except ValidationError as err:
    print(f"Error on Validator is: {err.errors()}")


# <-------------------------------------> 🟡 SERIALIZATION <------------------------------------->
# 🟡 Converting the "pydantinc model" into either in """Python""" or """JSON"""
# 🟡 These are usually run during the """data processing""", when converting a valid Python model into "dict" or "json"
class APIResponse(BaseModel):
    user_id: str
    secret_token: str
    password: str = Field(
        pattern="^[A-Za-z0-9]{6}$", serialization_alias="final_password"
    )

    # Use to apply custom transformation to individual fields during serialization
    @field_serializer("secret_token")
    def mask_token(self, token: str) -> str:
        return f"{token[:2]}***{token[-2:]}"

    # Overrides or wraps the serialization logic for entire model structure
    @model_serializer(mode="wrap")
    def add_metadata(self, handler):
        data = handler(self)
        data["status"] = "success"
        return data


try:
    api_response = APIResponse(
        user_id="id_123",
        password="kX7mP4",
        secret_token="sk-12322422424242ALHPQHahsfK",
    )

    # 🔶 Serialize to python using ".model_dump()"
    print("API Response with alias: ", api_response.model_dump(by_alias=True))
    print("API Response is: ", api_response.model_dump())
    print(
        "API Response by excluding password: ",
        api_response.model_dump(exclude={"password"}),
    )

    # 🔶 Serialize to JSON using ".model_dump_json()"
    print("API JSON Response is: ", api_response.model_dump_json())

    print(end="\n\n")
except ValidationError as err:
    print(f"Error happened on Serialization part {err.errors()}")


# <-------------------------------------> 🟡 BASE SETTINGS <------------------------------------->
# 🟡 For extracting and validation all the environment variables mention in the model
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
