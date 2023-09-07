from src.views.fast_sort import FastSortView


class FastSortController:

    def __init__(self, model: 'FastSortModel', widgets_factory, parent):
        self.model = model
        self.view = FastSortView(self, self.model, widgets_factory, parent)

        self.view.show()
        self.view.model_loaded()
