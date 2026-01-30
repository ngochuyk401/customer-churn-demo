import pandas as pd

def preprocess_input(data: dict) -> pd.DataFrame:
    """
    Tiền xử lý dữ liệu đầu vào từ giao diện người dùng
    """

    df = pd.DataFrame([data])

    # ========================
    # Chuẩn hóa Yes / No
    # ========================
    yes_no_cols = [
        'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling'
    ]

    for col in yes_no_cols:
        df[col] = df[col].map({'Có': 1, 'Không': 0})

    # SeniorCitizen
    df['SeniorCitizen'] = df['SeniorCitizen'].map({'Có': 1, 'Không': 0})

    # Gender
    df['gender'] = df['gender'].map({'Nam': 1, 'Nữ': 0})

    # ========================
    # Xử lý No internet service
    # ========================
    internet_cols = [
        'OnlineSecurity', 'OnlineBackup',
        'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies'
    ]

    for col in internet_cols:
        df[col] = df[col].replace({
            'Không có Internet': 'Không'
        })
        df[col] = df[col].map({'Có': 1, 'Không': 0})

    # MultipleLines
    df['MultipleLines'] = df['MultipleLines'].replace({
        'Không có DV điện thoại': 'Không'
    })
    df['MultipleLines'] = df['MultipleLines'].map({'Có': 1, 'Không': 0})

    # ========================
    # One-hot encoding
    # ========================
    df = pd.get_dummies(
        df,
        columns=['Contract', 'InternetService', 'PaymentMethod'],
        drop_first=True
    )

    return df
