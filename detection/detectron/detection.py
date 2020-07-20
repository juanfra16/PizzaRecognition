from ..abstract import AbstractPizzaDetector
import pandas as pd
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import cv2
import os

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg



class DetectronPizzaDetector(AbstractPizzaDetector):

    def load_model(self, weights_path="model_final.pth"):
        cfg = get_cfg()
        cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
        cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1  # only has one class (pizza)
        cfg.MODEL.WEIGHTS = os.path.join(".", weights_path)
        predictor = DefaultPredictor(cfg)
        return predictor

    def detect_pizzas_in_video(self, video_path: str) -> pd.DataFrame:
        """
        Método debe recibir el path a un video y como 
        output debe entregar un DataFrame con la siguiente estructura:

        frame, x1, y1, x2, y2

        Donde (x1, y1) es la esquina superior izquierda de la pizza
        y (x2, y2) es la esquina inferior derecha
        """

        predictor = self.load_model()
        names = ["frame", "x1", "y1", "x2", "y2"]
        example = pd.DataFrame(columns=names)
        vidcap = cv2.VideoCapture(video_path)
        success = True
        n_frame = 0
        while success:
            success, image = vidcap.read()
            if not success:
                break
            outputs = predictor(image)
            list_outputs = []
            for i in range(len(outputs["instances"])):
                list_outputs.append([n_frame,
                                     outputs["instances"].pred_boxes[i].tensor.tolist()[0][0],
                                     outputs["instances"].pred_boxes[i].tensor.tolist()[0][3],
                                     outputs["instances"].pred_boxes[i].tensor.tolist()[0][2],
                                     outputs["instances"].pred_boxes[i].tensor.tolist()[0][1]])
            aux = pd.DataFrame(list_outputs, columns=names)
            example = example.append(aux)
            n_frame += 1

        return example
