from src.views.tree_sort import TreeSortView


class TreeSortController:

    def __init__(self, model: 'TreeSortModel', widgets_factory, parent):
        self.model = model
        self.view = TreeSortView(self, self.model, widgets_factory, parent)

        self.view.show()
        self.view.model_loaded()
