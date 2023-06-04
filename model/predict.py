import pandas as pd
from tensorflow import keras
import autokeras as ak

MODEL_KERAS_PATH = './model/model_autokeras'
MODEL = keras.models.load_model(MODEL_KERAS_PATH, custom_objects=ak.CUSTOM_OBJECTS)

def predict_image(data):
    return MODEL.predict(data)