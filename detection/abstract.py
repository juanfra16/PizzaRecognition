"""
Define clase abstracta para los detectores
"""

from abc import ABC, abstractclassmethod
import pandas as pd


class AbstractPizzaDetector(ABC):

    @abstractclassmethod
    def detect_pizzas_in_video(self, video_path: str) -> pd.DataFame
    """
        Método debe recibir el path a un video y como 
        output debe entregar un DataFrame con la siguiente estructura:

        frame, x1, y1, x2, y2

        Donde (x1, y1) es la esquina superior izquierda de la pizza
        y (x2, y2) es la esquina inferior izquierda
        """
    pass
