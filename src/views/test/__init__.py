from typing import TypeVar

from PyQt6.QtWidgets import QWidget

from src.models import BaseModel
from src.utils.observer import DObserver
from src.models.sort import MenuItem, InputType
from src.utils.ts_meta import TSMeta
from src.views.test.static_ui import UiTest

ViewWidget = TypeVar('ViewWidget', bound=QWidget)
MenuItemModel = TypeVar('MenuItemModel', bound=BaseModel)


class TestView(QWidget, DObserver, metaclass=TSMeta):
    id: MenuItem

    def __init__(self, controller, model: MenuItemModel, widgets_factory, parent: ViewWidget):
        super().__init__(parent)
        self.id = model.id
        self.controller = controller
        self.model = model
        self.widgets_factory = widgets_factory

        parent.ui.content_layout.addWidget(self)
        parent.ui.content_layout.setCurrentWidget(self)

        self.ui = UiTest()
        self.ui.setup_ui(self, self.model.theme[0], widgets_factory)

        self.ui.test_header.setText(self.model.title)

        # Регистрация представлений
        self.model.add_observer(self)

        # События

    def model_changed(self):
        pass

    def model_loaded(self):
        self.model_changed()
