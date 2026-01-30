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

    df = align_columns(df)

    return df

EXPECTED_COLUMNS = [
    'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges',
    'gender_Male', 'Partner_Yes', 'Dependents_Yes', 'PhoneService_Yes',
    'MultipleLines_No phone service', 'MultipleLines_Yes',
    'InternetService_Fiber optic', 'InternetService_No',
    'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
    'OnlineBackup_No internet service', 'OnlineBackup_Yes',
    'DeviceProtection_No internet service', 'DeviceProtection_Yes',
    'TechSupport_No internet service', 'TechSupport_Yes',
    'StreamingTV_No internet service', 'StreamingTV_Yes',
    'StreamingMovies_No internet service', 'StreamingMovies_Yes',
    'Contract_One year', 'Contract_Two year', 'PaperlessBilling_Yes',
    'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check'
]

# Fix cột thiếu
def align_columns(df):
    for col in EXPECTED_COLUMNS:
        if col not in df.columns:
            df[col] = 0
    return df[EXPECTED_COLUMNS]

