import numpy as np
import pandas as pd
import seaborn as sns
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error


#functions
def num_pipeline_transformer(data):
    numerics = ['float64', 'int64']
    num_attrs= data.select_dtypes(include=numerics)
    num_pipeline=Pipeline([
        ('scaler', StandardScaler()),
    ])
    return num_attrs, num_pipeline

def pipeline_transformer(data):
    cat_attrs=["Origin"]
    num_attrs, num_pipeline = num_pipeline_transformer(data)
    full_pipeline= ColumnTransformer([
        ("num", num_pipeline, list(num_attrs)),
        ("cat", OneHotEncoder(), cat_attrs),
    ])
    prepared_data=full_pipeline.fit_transform(data)
    return prepared_data   

def predict_mpg(config,model):
    if type(config) is dict:
        df = pd.DataFrame(config)
    else:
        df = config

    preproc_data= pipeline_transformer(df)    
    print(len(preproc_data[0]))
    y_pred = model.predict(preproc_data)
    return y_pred

    