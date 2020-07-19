from .abstract import AbstractPizzaTracker
from video import Video

class CentroidTracker(AbstractPizzaTracker):
    def identify(self, metadata, window=50):
        """
        Metodo identifica pizzas unicas en la metadata

        Recibe un DataFrame de formato

        frame, x1, y1, x2, y2

        Y retorna un DataFrame de formato

        frame, label, x1, y1, x2, y2
        """
        video = Video(metadata)
        video.track(window=window)
        return video.to_df()
