from src.config import InIConfig
from src.models.sort import BaseSortModel
from src.utils.sort import SortType


class TreeSortModel(BaseSortModel):
    id: SortType = SortType.TREE
    title: str = 'Сортировка Деревом'

    def __init__(self, config: InIConfig, theme):

        self.config = config
        self.theme = theme

        # список наблюдателей
        self._mObservers = []

    def sort(self) -> None:
        pass
