from src.views.selection_sort import SelectionSortView


class SelectionSortController:

    def __init__(self, model: 'SelectionSortModel', widgets_factory, parent):
        self.model = model
        self.view = SelectionSortView(self, self.model, widgets_factory, parent)

        self.view.show()
        self.view.model_loaded()
