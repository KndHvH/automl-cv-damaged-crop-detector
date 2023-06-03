import pandas as pd
from pycaret.classification import *


MODEL_PKL_PATH='./model/pickle_pycaret'
MODEL = load_model(MODEL_PKL_PATH)

def predict(data):
    return predict_model(MODEL, data = data, raw_score = True)

def predict_image(image):
    img_row = image.reshape(1, -1)
    df = pd.DataFrame(img_row, columns=[f"pixel_{i}" for i in range(img_row.shape[1])])
    

    return predict(df)