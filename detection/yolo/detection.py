from ..abstract import AbstractPizzaDetector
import pandas as pd
from .detect_arara import detect
import os
import shutil
from sys import platform
import os

class Opt:
    def __init__(self,cfg, names, weights, source, output, img_size, conf_thres,
                               iou_thres, fourcc, half, device, view_img, save_txt,
                               agnostic_nms, augment, classes):
        self.cfg = cfg
        self.names = names
        self.weights = weights
        self.source = source
        self.output = output
        self.img_size = img_size
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self.fourcc = fourcc
        self.half = half
        self.device = device
        self.view_img = view_img
        self.save_txt = save_txt
        self.agnostic_nms = agnostic_nms
        self.augment = augment
        self.classes = classes

class YoloPizzaDetector(AbstractPizzaDetector):

    def detect_pizzas_in_video(self, video_path: str, cfg='cfg/yolov3-spp.cfg', names='data/arara.names',
                               weights='weights/arara_yolov3.pt', output='output', img_size=512, conf_thres=0.3,
                               iou_thres=0.6, fourcc='mp4v', half=False, device='', view_img=False, save_txt=True,
                               agnostic_nms=False, augment=False, classes=None) -> pd.DataFrame:
        """
        Método debe recibir el path a un video y como 
        output debe entregar un DataFrame con la siguiente estructura:

        frame, x1, y1, x2, y2

        Donde (x1, y1) es la esquina superior izquierda de la pizza
        y (x2, y2) es la esquina inferior derecha
        """
        os.mkdir("temporal")
        #if platform in ['linux', 'darwin']:
        #    sep = "/"
        #else:
        #    sep = "\"
        rvideo = reversed(video_path)
        aux = rvideo[rvideo.find("/"):]
        path = reversed(aux)
        new_path = os.path.join("temporal", path)
        shutil.copy2(video_path, new_path)
        source = "temporal"
        opt = Opt(cfg ,names ,weights , source, output, img_size, conf_thres,
                               iou_thres, fourcc, half, device, view_img, save_txt,
                               agnostic_nms, augment, classes)
        a = detect(opt)
        # Ahora esta creada una copia en la carpeta temporal. Su path es new_path
        return a.values()
