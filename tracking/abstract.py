from abc import ABC, abstractmethod
import pandas as pd


class AbstractPizzaTracker(ABC):

    @abstractmethod
    def identify(self, metadata: pd.DataFrame) -> pd.DataFrame:
        """
        Metodo identifica pizzas unicas en la metadata

        Recibe un DataFrame de formato

        frame, x1, y1, x2, y2

        Y retorna un DataFrame de formato

        frame, label, x1, y1, x2, y2
        """
        pass
