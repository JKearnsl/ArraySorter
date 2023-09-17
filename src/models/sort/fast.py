from src.config import InIConfig
from src.models.sort import BaseSortModel
from src.utils.sort import SortType


class FastSortModel(BaseSortModel):
    id: SortType = SortType.FAST
    title: str = 'Быстрая Сортировка'

    def __init__(self, config: InIConfig, theme):

        self.config = config
        self.theme = theme

        # список наблюдателей
        self._mObservers = []

    def sort(self) -> None:
        pass
