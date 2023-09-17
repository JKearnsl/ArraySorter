from src.config import InIConfig
from src.models.sort import BaseSortModel
from src.models.sort import MenuItem


class ShellSortModel(BaseSortModel):
    id: MenuItem = MenuItem.SHELL
    title: str = 'Сортировка Шелла'

    def __init__(self, config: InIConfig, theme):

        self.config = config
        self.theme = theme

        # список наблюдателей
        self._mObservers = []

    def sort(self) -> None:
        pass
