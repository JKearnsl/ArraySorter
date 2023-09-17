from typing import TypeVar

from PyQt6.QtWidgets import QWidget

from src.utils.observer import DObserver
from src.utils.sort import SortType
from src.utils.ts_meta import TSMeta
from src.views.sort.static_ui import UiSort
from src.models.sort import BaseSortModel

ViewWidget = TypeVar('ViewWidget', bound=QWidget)


class SortView(QWidget, DObserver, metaclass=TSMeta):
    id: SortType

    def __init__(self, controller, model: BaseSortModel, widgets_factory, parent: ViewWidget):
        super().__init__(parent)
        self.id = model.id
        self.controller = controller
        self.model = model
        self.widgets_factory = widgets_factory

        parent.ui.content_layout.addWidget(self)
        parent.ui.content_layout.setCurrentWidget(self)

        self.ui = UiSort()
        self.ui.setup_ui(self, self.model.theme[0], widgets_factory)

        self.ui.sort_header.setText(self.model.title)

        # Регистрация представлений
        self.model.add_observer(self)

        # События

    def model_changed(self):
        pass

    def model_loaded(self):
        self.model_changed()
