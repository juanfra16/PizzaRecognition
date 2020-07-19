import pandas as pd



class Rectangulo:

    count = 0

    def __init__(self, frame, x1, y1, x2, y2):
        self.frame = frame
        self.x = (x1 + x2)/2
        self.y = (y1 + y2)/2
        self.width = abs(x2-x1)
        self.height = abs(y2-y1)
        self.supizq = x1, y1
        self.infder = x2, y2
        self.num = Rectangulo.count
        self.label = None
        Rectangulo.count += 1

    def __repr__(self):
        return "{} : {},{},{},{} |".format(self.frame,*self.supizq,
                                           *self.infder)

    def intersect(self, other, window=100):
        assert isinstance(other, Rectangulo), "Deben ser ambos Rectangulos"
        if abs(self.frame - other.frame) > window:
            return False
        if other.x < self.supizq[0] or other.x > self.infder[0]:
            return False
        elif other.y < self.supizq[1] or other.y > self.infder[1]:
            return False
        else:
            return True

    def setLabel(self, label):
        self.label = label

    def hasLabel(self):
        return self.label is not None and isinstance(self.label, Label)

    def to_df(self):
        return pd.DataFrame({
                "frame": self.frame,
                "label": self.label.name if self.hasLabel() else "",
                "x1": self.supizq[0],
                "y1": self.supizq[1],
                "x2": self.infder[0],
                "y2": self.infder[1]
            }, index=[self.num])
