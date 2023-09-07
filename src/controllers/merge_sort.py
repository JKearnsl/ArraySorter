from src.views.merge_sort import MergeSortView


class MergeSortController:

    def __init__(self, model: 'MergeSortModel', widgets_factory, parent):
        self.model = model
        self.view = MergeSortView(self, self.model, widgets_factory, parent)

        self.view.show()
        self.view.model_loaded()
