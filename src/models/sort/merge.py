from src.config import InIConfig
from src.models.sort import BaseSortModel
from src.utils.sort import SortType


class MergeSortModel(BaseSortModel):
    id: SortType = SortType.MERGE
    title: str = 'Сортировка Слиянием'

    def __init__(self, config: InIConfig, theme):

        self.config = config
        self.theme = theme

        # список наблюдателей
        self._mObservers = []

    def sort(self) -> None:
        pass

    def add_observer(self, observer):
        self._mObservers.append(observer)

    def remove_observer(self, observer):
        self._mObservers.remove(observer)

    def notify_observers(self):
        for observer in self._mObservers:
            observer.model_changed()
