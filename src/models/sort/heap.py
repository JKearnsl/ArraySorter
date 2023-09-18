from src.config import InIConfig
from src.models.sort import BaseSortModel
from src.models.sort import MenuItem


class HeapSortModel(BaseSortModel):
    id: MenuItem = MenuItem.HEAP
    title: str = 'Пирамидальная Сортировка'
    complexity: str = 'O(n^2)'

    def __init__(self, config: InIConfig, theme):

        self.config = config
        self.theme = theme

        # список наблюдателей
        self._mObservers = []

    def sort(self) -> None:
        pass
