from langchain.schema import BaseMessage
from langchain_core.language_models import BaseChatModel
from abc import ABC, abstractmethod


class LlmProviderService(ABC):
    model: BaseChatModel

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.model = self._create_model()

    @abstractmethod
    def _create_model(self):
        pass

    def infer(self, messages: list[BaseMessage]):
        return self.model.invoke(messages)
