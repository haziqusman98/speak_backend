from django.apps import AppConfig
import pathlib
import os
from .model.predictor import Predictor

current_path = os.path.dirname(__file__)
model_folder = os.path.join(current_path, "model")
class TexttoaslConfig(AppConfig):
    name = 'textToAsl'
    model_pth = os.path.join(model_folder,"nslt_100_004272_0.686441.pt")
    label_pth = os.path.join(model_folder,"wlasl_class_list.txt")
    predictor = Predictor(model_path=model_pth,label_path=label_pth)
