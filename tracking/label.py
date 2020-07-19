class Label:


    def __init__(self, rectangulos=None, video=None):
        assert rectangulos is None or isinstance(rectangulos, list)
        self.name = next(video.name)
        self.rectangulos = [] if rectangulos is None else rectangulos

    def addRectangulo(self, rect):
        if rect not in self.rectangulos:
            rect.setLabel(self)
            self.rectangulos.append(rect)

    def rectIntersects(self, rect, window=100):
        return bool(len(list(filter(lambda x: x.intersect(rect, window),
                                    self.rectangulos))))

    def to_df(self):
        df = pd.concat(map(lambda x: x.to_df(), self.rectangulos))
        df["label"] = self.name
        return df
    
