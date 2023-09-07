from src.views.exchange_sort import ExchangeSortView


class ExchangeSortController:

    def __init__(self, model: 'ExchangeSortModel', widgets_factory, parent):
        self.model = model
        self.view = ExchangeSortView(self, self.model, widgets_factory, parent)

        self.view.show()
        self.view.model_loaded()
