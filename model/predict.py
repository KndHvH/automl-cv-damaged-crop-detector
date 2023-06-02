import pandas as pd
from pycaret.classification import *

MODEL_PKL_PATH='./model/pickle_pycaret'
MODEL = load_model(MODEL_PKL_PATH)

def predict(data):
    return predict_model(MODEL, data = data, raw_score = True)


def format_image(image):
    image.reshape(image.shape[0], -1)