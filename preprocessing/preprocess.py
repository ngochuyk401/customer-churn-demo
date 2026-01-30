import pandas as pd

# =========================
# CÁC CỘT MÀ MÔ HÌNH CẦN
# =========================
EXPECTED_COLUMNS = [
    'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges',

    'gender_Male',

    'Partner_Yes', 'Dependents_Yes', 'PhoneService_Yes',

    'MultipleLines_No phone service', 'MultipleLines_Yes',

    'InternetService_Fiber optic', 'InternetService_No',

    'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
    'OnlineBackup_No internet service', 'OnlineBackup_Yes',
    'DeviceProtection_No internet service', 'DeviceProtection_Yes',
    'TechSupport_No internet service', 'TechSupport_Yes',
    'StreamingTV_No internet service', 'StreamingTV_Yes',
    'StreamingMovies_No internet service', 'StreamingMovies_Yes',

    'Contract_One year', 'Contract_Two year',

    'PaperlessBilling_Yes',

    'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check',
    'PaymentMethod_Mailed check'
]

# =========================
# TIỀN XỬ LÝ ĐẦU VÀO
# =========================
def preprocess_input(data: dict) -> pd.DataFrame:
    """
    data: dict với VALUE ĐÚNG THEO DATASET GỐC (TIẾNG ANH)
    """

    df = pd.DataFrame([data])

    # =========================
    # Numeric
    # =========================
    df['SeniorCitizen'] = int(df.loc[0, 'SeniorCitizen'])
    df['tenure'] = float(df.loc[0, 'tenure'])
    df['MonthlyCharges'] = float(df.loc[0, 'MonthlyCharges'])
    df['TotalCharges'] = float(df.loc[0, 'TotalCharges'])

    # =========================
    # Gender
    # =========================
    df['gender_Male'] = 1 if df.loc[0, 'gender'] == 'Male' else 0

    # =========================
    # Yes / No columns
    # =========================
    yes_no_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
    for col in yes_no_cols:
        df[f'{col}_Yes'] = 1 if df.loc[0, col] == 'Yes' else 0

    # =========================
    # MultipleLines
    # =========================
    df['MultipleLines_Yes'] = 1 if df.loc[0, 'MultipleLines'] == 'Yes' else 0
    df['MultipleLines_No phone service'] = 1 if df.loc[0, 'MultipleLines'] == 'No phone service' else 0

    # =========================
    # InternetService
    # =========================
    df['InternetService_Fiber optic'] = 1 if df.loc[0, 'InternetService'] == 'Fiber optic' else 0
    df['InternetService_No'] = 1 if df.loc[0, 'InternetService'] == 'No' else 0

    # =========================
    # Các dịch vụ Internet
    # =========================
    internet_services = [
        'OnlineSecurity', 'OnlineBackup',
        'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies'
    ]

    for col in internet_services:
        df[f'{col}_Yes'] = 1 if df.loc[0, col] == 'Yes' else 0
        df[f'{col}_No internet service'] = 1 if df.loc[0, col] == 'No internet service' else 0

    # =========================
    # Contract
    # =========================
    df['Contract_One year'] = 1 if df.loc[0, 'Contract'] == 'One year' else 0
    df['Contract_Two year'] = 1 if df.loc[0, 'Contract'] == 'Two year' else 0
    # Month-to-month -> cả 2 = 0 (CHUẨN)

    # =========================
    # PaymentMethod
    # =========================
    df['PaymentMethod_Credit card (automatic)'] = 1 if df.loc[0, 'PaymentMethod'] == 'Credit card (automatic)' else 0
    df['PaymentMethod_Electronic check'] = 1 if df.loc[0, 'PaymentMethod'] == 'Electronic check' else 0
    df['PaymentMethod_Mailed check'] = 1 if df.loc[0, 'PaymentMethod'] == 'Mailed check' else 0
    # Bank transfer (automatic) -> cả 3 = 0 (CHUẨN)

    # =========================
    # ĐẢM BẢO ĐỦ CỘT + ĐÚNG THỨ TỰ
    # =========================
    df_final = df.reindex(columns=EXPECTED_COLUMNS, fill_value=0)

    return df_final
