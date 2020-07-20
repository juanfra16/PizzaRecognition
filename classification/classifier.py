import tensorflow as tf
import numpy as np
import pandas as pd
import cv2


class PizzaClassifier:

    def __init__(self, model, classes: list, target_size=224):
        self.model = self.load_model(model)
        self.classes = classes # Nombres de las clases. Ej: ['before_cut', 'during_cut', 'done']
        self.target_size = target_size
    
    @staticmethod
    def resize_pizza(pizza, target_size):
        pizza_size = np.array(pizza.shape[:2])

        fx, fy = target_size / pizza_size
        scaling_factor = min(fx, fy)
        pizza_resized = cv2.resize(pizza, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_CUBIC)

        bottom_padding = target_size - pizza_resized.shape[0]
        right_padding = target_size - pizza_resized.shape[1]

        pizza_padded = cv2.copyMakeBorder(pizza_resized, 
                                          0, bottom_padding, 
                                          0, right_padding, 
                                          cv2.BORDER_CONSTANT, value=(0,0,0))
        
        #print(pizza_padded.shape)

        return pizza_padded.reshape([1, *(pizza_padded.shape)]).astype(np.float32)

    def classify_pizzas(self, video_path: str, metadata: pd.DataFrame) -> pd.DataFrame:
        """
        Método recibe el path a un video y un DataFrame de metadata 
        de formato

        frame, label, x1, y1, x2, y2

        Y retorna un DataFrame con formato
        
        frame, label, x1, y1, x2, y2, pizza_state
        """

        video = cv2.VideoCapture(video_path)
        pizza_states = []

        for index, row in metadata.iterrows():

          # Get frame
          video.set(1, row.frame)
          _, frame = video.read()

          #print(frame.shape())

          # Extract pizza
          top = max(0, row.y1)
          bottom = min(frame.shape[0], row.y2)
          left = max(0, row.x1)
          right = min(frame.shape[1], row.x2)

          frame_pizza = frame[int(top):int(bottom), int(left):int(right)]

          # Resize frame
          resized_pizza = self.resize_pizza(frame_pizza, self.target_size)
          
          pizza_states.append(self.classes[model.predict(resized_pizza).argmax(axis=1)[0]])
        
        df_out = metadata.copy()
        df_out["pizza_state"] = pizza_states

        return df_out
      
    def load_model(self, model_path):
        if type(model_path) is str:
            self.model = tf.keras.models.load_model(model_path)
        else: 
            self.model = model
