from src.config import InIConfig
from src.models.sort import BaseSortModel
from src.models.sort import SortType


class InsertionSortModel(BaseSortModel):
    id: SortType = SortType.INSERTION
    title: str = 'Сортировка Вставками'

    def __init__(self, config: InIConfig, theme):

        self.config = config
        self.theme = theme

        # список наблюдателей
        self._mObservers = []

    def sort(self) -> None:
        pass
