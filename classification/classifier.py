import pandas as pd


class PizzaClassifier:

    def __init__(self, model, classes: list):
        self.model = model
        self.classes = classes # Nombres de las clases. Ej: ['before_cut', 'during_cut', 'done']

    def classify_pizzas(self, video_path: str, metadata: pd.DataFrame) -> pd.DataFrame:
        """
        Método recibe el path a un video y un DataFrame de metadata 
        de formato

        frame, label, x1, y1, x2, y2

        Y retorna un DataFrame con formato
        
        frame, label, x1, y1, x2, y2, pizza_state
        """
        pass
