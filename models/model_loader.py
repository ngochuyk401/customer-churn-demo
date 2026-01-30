import joblib
import os

BASE_DIR = os.path.dirname(__file__)

def load_model(model_name: str):
    if model_name == "Random Forest":
        path = os.path.join(BASE_DIR, "rf_tuned_model.pkl")
    elif model_name == "KNN":
        path = os.path.join(BASE_DIR, "knn_model.pkl")
    elif model_name == "SVM":
        path = os.path.join(BASE_DIR, "svm_model.pkl")
    else:
        raise ValueError("Mô hình không hợp lệ")

    return joblib.load(path)
