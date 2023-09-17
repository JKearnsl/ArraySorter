from abc import abstractmethod, ABC

from src.models import BaseModel
from src.utils.sort import SortType


class BaseSortModel(BaseModel):
    id: SortType
    title: str

    def set_list(self, string_list: str) -> None:
        pass

    def gen_list(self, count_of_elements: int) -> None:
        pass

    @abstractmethod
    def sort(self) -> None:
        pass
