![Detectron](https://raw.githubusercontent.com/facebookresearch/detectron2/master/.github/Detectron2-Logo-Horz.svg)
Detector de pizzas usando [Detectron2](https://github.com/facebookresearch/detectron2)

El método recibe un path hacia un vídeo y retorna un DataFrame con la estructura (n_frame, x1, y1, x2, y2) donde
cada fila representa una pizza reconocida con n_frame el numero de frame dentro del video, x1, y1 la esquina superior
izquierda de la bounding-box de la pizza y x2, y2 la esquina inferior derecha.

## Requerimientos
* torch 1.5
* torchvision 0.6
* cython pyyaml 5.1
* numpy
* cv2
* detectron2 0.1.3 . Instalacion via pip con:
 
  `pip install detectron2==0.1.3 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/index.html`

### Descarga de pesos para el modelo
Los pesos de Detectron2 con finetuning están disponibles en este [link](https://drive.google.com/drive/u/0/folders/1B7_vB5lWDhnGkpCB-_FhjosgxH_uyymx).
El archivo correspondiente es `detectron_mode_final.pth`. Luego, el path a los pesos se entrega como argumento 
`weights_path=path_to_weights` al iniciar la clase `DetectronPizzaDetector`. 




