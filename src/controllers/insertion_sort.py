from src.views.insertion_sort import InsertionSortView


class InsertionSortController:

    def __init__(self, model: 'InsertionSortModel', widgets_factory, parent):
        self.model = model
        self.view = InsertionSortView(self, self.model, widgets_factory, parent)

        self.view.show()
        self.view.model_loaded()
