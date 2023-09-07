from src.controllers.exchange_sort import ExchangeSortController
from src.controllers.fast_sort import FastSortController
from src.controllers.heap_sort import HeapSortController
from src.controllers.merge_sort import MergeSortController
from src.controllers.settings import SettingsController
from src.controllers.insertion_sort import InsertionSortController
from src.controllers.selection_sort import SelectionSortController
from src.controllers.shell_sort import ShellSortController
from src.controllers.tree_sort import TreeSortController
from src.models.exchange_sort import ExchangeSortModel
from src.models.fast_sort import FastSortModel
from src.models.heap_sort import HeapSortModel
from src.models.merge_sort import MergeSortModel

from src.models.settings import SettingsModel
from src.models.insertion_sort import InsertionSortModel
from src.models.main import MainModel
from src.models.selection_sort import SelectionSortModel
from src.models.shell_sort import ShellSortModel
from src.models.tree_sort import TreeSortModel
from src.views.main import MainView


class MainController:

    def __init__(self, model: 'MainModel', widgets_factory: 'WidgetsFactory'):
        self.model = model
        self.widgets_factory = widgets_factory
        self.view = MainView(self, self.model, widgets_factory)

        self.view.show()
        self.view.model_loaded()

    def show_settings(self):
        controller = SettingsController(
            SettingsModel(self.model.config, self.model.theme), self.widgets_factory, self.view
        )

    def load_insertion_sort(self):
        controller = InsertionSortController(
            InsertionSortModel(self.model.config, self.model.theme), self.widgets_factory, self.view
        )

    def load_selection_sort(self):
        controller = SelectionSortController(
            SelectionSortModel(self.model.config, self.model.theme), self.widgets_factory, self.view
        )

    def load_exchange_sort(self):
        controller = ExchangeSortController(
            ExchangeSortModel(self.model.config, self.model.theme), self.widgets_factory, self.view
        )

    def load_fast_sort(self):
        controller = FastSortController(
            FastSortModel(self.model.config, self.model.theme), self.widgets_factory, self.view
        )

    def load_tree_sort(self):
        controller = TreeSortController(
            TreeSortModel(self.model.config, self.model.theme), self.widgets_factory, self.view
        )

    def load_heap_sort(self):
        controller = HeapSortController(
            HeapSortModel(self.model.config, self.model.theme), self.widgets_factory, self.view
        )

    def load_shell_sort(self):
        controller = ShellSortController(
            ShellSortModel(self.model.config, self.model.theme), self.widgets_factory, self.view
        )

    def load_merge_sort(self):
        controller = MergeSortController(
            MergeSortModel(self.model.config, self.model.theme), self.widgets_factory, self.view
        )
