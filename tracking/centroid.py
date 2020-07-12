from .abstract import AbstractPizzaTracker


class CentroidTracker(AbstractPizzaTracker):
    def identify(self, metadata):
        """
        Metodo identifica pizzas unicas en la metadata

        Recibe un DataFrame de formato

        frame, x1, y1, x2, y2

        Y retorna un DataFrame de formato

        frame, label, x1, y1, x2, y2
        """
        return super().identify(metadata)
