from langchain_openai import ChatOpenAI
from constants.envs import API_KEYS, ApiKeyNames
from .llm_provider_service import LlmProviderService


class OpenRouterService(LlmProviderService):
    def __init__(
        self,
        model_name: str,
    ):
        super().__init__(model_name)

    def _create_model(self):
        return ChatOpenAI(
            model_name=self.model_name,
            openai_api_base="https://openrouter.ai/api/v1",
            openai_api_key=API_KEYS[ApiKeyNames.OPENROUTER],
        )


def create_openrouter_service(model_name: str) -> OpenRouterService:
    return OpenRouterService(model_name=model_name)


__all__ = ["create_openrouter_service"]
