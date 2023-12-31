from abc import ABCMeta, abstractmethod


class DObserver(metaclass=ABCMeta):

    @abstractmethod
    def model_changed(self):
        """
        Метод, который будет вызван у наблюдателя при изменении модели.
        """
        pass
