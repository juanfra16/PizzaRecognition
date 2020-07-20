from ..abstract import AbstractPizzaDetector
import pandas as pd


class YoloPizzaDetector(AbstractPizzaDetector):

    def detect_pizzas_in_video(self, video_path: str) -> pd.DataFrame:
        """
        Método debe recibir el path a un video y como 
        output debe entregar un DataFrame con la siguiente estructura:

        frame, x1, y1, x2, y2

        Donde (x1, y1) es la esquina superior izquierda de la pizza
        y (x2, y2) es la esquina inferior derecha
        """
        names = ["frame", "x1", "y1", "x2", "y2"]
        example = pd.DataFrame(columns=names)
        return example
