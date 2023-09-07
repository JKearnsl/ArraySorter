from PyQt6.QtWidgets import QWidget

from src.utils.observer import DObserver
from src.utils.ts_meta import TSMeta
from src.views.main.static_ui import UiMainWindow
from src.models.main import MainModel
from src.views.widgets import WidgetsFactory


class MainView(QWidget, DObserver, metaclass=TSMeta):

    def __init__(self, controller, model: MainModel, widgets_factory: WidgetsFactory, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.model = model

        self.ui = UiMainWindow()
        self.ui.setup_ui(
            self,
            theme_class=model.theme[0],
            widgets_factory=widgets_factory,
            version=self.model.config.VAR.VERSION,
            app_name=self.model.config.VAR.BASE.APP_NAME,
            debug=self.model.config.VAR.BASE.DEBUG
        )

        # Регистрация представлений
        self.model.add_observer(self)

        # События
        self.ui.menu_select_model.currentChanged.connect(self.menu_select_changed)
        self.ui.menu_settings_button.clicked.connect(self.controller.show_settings)

    def model_changed(self):
        pass

    def model_loaded(self):
        self.ui.menu_list_widget.setCurrentIndex(self.ui.menu_list_widget.model().index(0, 0))

    def menu_select_changed(self, *args):
        index = self.ui.menu_list_widget.currentIndex().row()
        item = self.ui.menu_list_widget.model().item(index)

        if self.ui.content_layout.count() > 0:
            self.ui.content_layout.setCurrentIndex(0)
            current_widget = self.ui.content_layout.currentWidget()
            if current_widget.id == item.id:
                return

            # Кэш
            for i in range(self.ui.content_layout.count()):
                widget = self.ui.content_layout.widget(i)
                if widget.id == item.id:
                    self.ui.content_layout.setCurrentWidget(widget)
                    return

        if item.id == "insertion_sort":
            self.controller.load_insertion_sort()
        elif item.id == "selection_sort":
            self.controller.load_selection_sort()
        elif item.id == "exchange_sort":
            self.controller.load_exchange_sort()
        elif item.id == "fast_sort":
            self.controller.load_fast_sort()
        elif item.id == "tree_sort":
            self.controller.load_tree_sort()
        elif item.id == "heap_sort":
            self.controller.load_heap_sort()
        elif item.id == "shell_sort":
            self.controller.load_shell_sort()
        elif item.id == "merge_sort":
            self.controller.load_merge_sort()
        else:
            raise ValueError(f"Unknown menu item: {item.id!r}")
