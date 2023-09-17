import psutil

from src.config import InIConfig


class MainModel:

    def __init__(self, config: InIConfig, theme: tuple[type, str, str]):
        self.config = config
        self.theme = theme

        # список наблюдателей
        self._mObservers = []

    def get_ram_usage(self) -> int:
        return int(psutil.Process().memory_info().rss / (1024 * 1024))

    def add_observer(self, observer):
        self._mObservers.append(observer)

    def remove_observer(self, observer):
        self._mObservers.remove(observer)

    def notify_observers(self):
        for observer in self._mObservers:
            observer.model_changed()
