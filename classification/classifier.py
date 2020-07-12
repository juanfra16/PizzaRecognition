import pandas as pd


class PizzaClassifier:

    def __init__(self, model, target_label=2):
        self.model = model
        self.target_label = target_label

    def classify_pizzas(self, video_path: str, metadata: pd.DataFrame) -> pd.DataFrame:
        """
        Método recibe el path a un video y un DataFrame de metadata 
        de formato

        frame, label, x1, y1, x2, y2

        Y retorna un DataFrame del mismo formato pero solo con pizzas
        que fueron classificadas como listas
        """
        pass
