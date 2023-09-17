from src.config import InIConfig
from src.models.sort import BaseSortModel
from src.models.sort import SortType


class SelectionSortModel(BaseSortModel):
    id: SortType = SortType.SELECT
    title: str = 'Сортировка Выбором'

    def __init__(self, config: InIConfig, theme):

        self.config = config
        self.theme = theme

        self._list = []

        # список наблюдателей
        self._mObservers = []

    def sort(self) -> None:
        pass
