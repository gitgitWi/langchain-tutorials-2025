from enum import StrEnum
from typing import Final
from environs import env, validate
from pydantic import SecretStr

env.read_env()


class ApiKeyNames(StrEnum):
    OPENROUTER = "OPENROUTER"


API_KEYS: Final[dict[ApiKeyNames, SecretStr | None]] = {
    ApiKeyNames.OPENROUTER: SecretStr(
        env("OPENROUTER_API_KEY", validate=validate.Length(min=2), default=None)
    ),
}
