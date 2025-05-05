import pickle
import os
import re
import numpy as np
import logging
import joblib
from app.utils.preprocess import preprocess_url_single


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  
        
def load_model():
    try:
        model_path = "app/models/model.pkl"
        with open(model_path, "rb") as f:
            model = joblib.load(f)
        return model
    except Exception as e:
        import traceback
        logger.error("Model failed to load")
        logger.error(traceback.format_exc())  # <-- Add this
        return None



def predict(model, url: str):
    features = preprocess_url_single(url)
    return model.predict(features)[0]
