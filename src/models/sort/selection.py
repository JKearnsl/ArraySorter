from src.config import InIConfig
from src.models.sort import BaseSortModel
from src.models.sort import MenuItem


class SelectionSortModel(BaseSortModel):
    id: MenuItem = MenuItem.SELECT
    title: str = 'Сортировка Выбором'

    def __init__(self, config: InIConfig, theme):

        self.config = config
        self.theme = theme

        self._list = []

        # список наблюдателей
        self._mObservers = []

    def sort(self) -> None:
        pass
