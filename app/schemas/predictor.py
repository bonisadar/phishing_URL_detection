
import pickle
import os
import re
import numpy as np
import logging
import joblib

'''def load_model():
    model_path = os.getenv("MODEL_PATH", "model.pkl")
    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None'''

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

'''
def preprocess_url_single(url: str):
    # 1. Remove spaces
    url = url.replace(' ', '')
    if len(url) < 3:
        raise ValueError("URL too short after removing spaces.")

    # 2. Remove protocol (http, https, etc.)
    url = re.sub(r'^(http://|https://|https|http)', '', url, flags=re.IGNORECASE)
    url = url.lstrip('.').strip('/').strip()

    # 3. Extract FQDN (first part before any "/")
    fqdn = url.split('/')[0]
    fqdn = fqdn.rstrip('.')  # Remove trailing dots

    # Features:
    len_url = len(url)
    len_fqdn = len(fqdn)

    # TLD
    tld = fqdn.split('.')[-1] if '.' in fqdn else ''
    len_tld = len(tld)

    # Contains IP
    ipv4_pattern = r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)'
    ipv6_pattern = r'(\[[0-9a-fA-F:]+\])'
    contains_ip = int(bool(re.search(f"{ipv4_pattern}|{ipv6_pattern}", url)))

    # Entropy
    def calculate_entropy(s):
        probs = [float(s.count(c)) / len(s) for c in set(s)]
        return -sum([p * np.log2(p) for p in probs])

    url_entropy = calculate_entropy(url)
    fqdn_entropy = calculate_entropy(fqdn)

    # Capital letters in FQDN
    fqdn_capitals = len(re.findall(r'[A-Z]', fqdn))

    # Character/Number ratio
    chars = sum(x.isalpha() for x in url)
    digits = sum(x.isdigit() for x in url)
    char_num_ratio = chars / digits if digits != 0 else 0

    # Pack features into a vector
    features = np.array([
        len_url,
        len_fqdn,
        len_tld,
        contains_ip,
        url_entropy,
        fqdn_entropy,
        fqdn_capitals,
        char_num_ratio
    ]).reshape(1, -1)

    return features

'''

def predict(model, url: str):
    features = preprocess_url_single(url)
    return model.predict(features)[0]
