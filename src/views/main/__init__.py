from PyQt6.QtWidgets import QWidget
from apscheduler.schedulers.qt import QtScheduler

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

        self.scheduler = QtScheduler()
        self.scheduler.add_job(self.memory_usage_tick, 'interval', seconds=3)
        self.scheduler.start()

        # Регистрация представлений
        self.model.add_observer(self)

        # События
        self.ui.menu_select_model.currentChanged.connect(self.menu_select_changed)
        self.ui.menu_settings_button.clicked.connect(self.controller.show_settings)

    def model_changed(self):
        pass

    def memory_usage_tick(self):
        self.ui.memory_usage_label.setText(f"ОЗУ: {self.model.get_ram_usage()} МБ")

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

        self.controller.show_sort(item.id)
