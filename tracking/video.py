import pandas as pd
from label import Label
from rect import Rectangulo

def labelGen():
    i = 0
    while True:
        yield f"pizza{i}"
        i += 1

def vidGen():
    while True:
        yield labelGen()

class Video:

    nombres = vidGen()

    def __init__(self, df):
        self.df = df
        self.name = next(Video.nombres)
        self.labels = None

    def track(self, window=100):
        #inicio = datetime.now()
        minimo = self.df.frame.min()
        rects = list(map(lambda x: Rectangulo(*x), self.df.values))
        labels = []
        for i in range(len(rects)):
            salta = False
            for k in range(len(labels)):
                if labels[k].rectIntersects(rects[i], window):
                    labels[k].addRectangulo(rects[i])
                    salta = True
            if not salta:
                for j in range(len(rects)):
                    if i == j:
                        continue
                    elif rects[i].intersect(rects[j]):
                        ambos = [rects[i], rects[j]]
                        tieneLab = list(filter(lambda x: x.hasLabel(), ambos))
                        if len(tieneLab) == 1:
                            tieneLab = tieneLab[0]
                            ambos.remove(tieneLab)
                            tieneLab.label.addRectangulo(ambos[0])
                        else:
                            label = Label(video=self)
                            label.addRectangulo(rects[i])
                            label.addRectangulo(rects[j])
                            labels.append(label)
        self.labels = labels
        #return (datetime.now()-inicio)/self.df.frame.size

    def to_df(self):
        if self.labels is not None:
            return pd.concat(map(lambda x: x.to_df(), self.labels))
