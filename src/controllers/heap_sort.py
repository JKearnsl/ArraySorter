from src.views.heap_sort import HeapSortView


class HeapSortController:

    def __init__(self, model: 'HeapSortModel', widgets_factory, parent):
        self.model = model
        self.view = HeapSortView(self, self.model, widgets_factory, parent)

        self.view.show()
        self.view.model_loaded()
