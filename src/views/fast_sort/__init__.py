from typing import TypeVar

from PyQt6.QtWidgets import QWidget

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.views.fast_sort.static_ui import UiFastSort
from src.models.fast_sort import FastSortModel

ViewWidget = TypeVar('ViewWidget', bound=QWidget)


class FastSortView(QWidget, DObserver, metaclass=TSMeta):
    id: str = "fast_sort"

    def __init__(self, controller, model: FastSortModel, widgets_factory, parent: ViewWidget):
        super().__init__(parent)
        self.controller = controller
        self.model = model
        self.widgets_factory = widgets_factory

        parent.ui.content_layout.addWidget(self)
        parent.ui.content_layout.setCurrentWidget(self)

        self.ui = UiFastSort()
        self.ui.setup_ui(self, self.model.theme[0], widgets_factory)

        # Регистрация представлений
        self.model.add_observer(self)

        # События

    def model_changed(self):
        pass

    def model_loaded(self):
        self.model_changed()
