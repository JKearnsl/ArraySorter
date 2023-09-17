from src.config import InIConfig
from src.models.sort import BaseSortModel
from src.models.sort import SortType


class ExchangeSortModel(BaseSortModel):
    id: SortType = SortType.EXCHANGE
    title: str = 'Сортировка Обменом'

    def __init__(self, config: InIConfig, theme):

        self.config = config
        self.theme = theme

        # список наблюдателей
        self._mObservers = []

    def sort(self) -> None:
        pass
