from src.views.shell_sort import ShellSortView


class ShellSortController:

    def __init__(self, model: 'ShellSortModel', widgets_factory, parent):
        self.model = model
        self.view = ShellSortView(self, self.model, widgets_factory, parent)

        self.view.show()
        self.view.model_loaded()
