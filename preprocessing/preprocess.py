import pandas as pd

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
    'PaymentMethod_Electronic check',
    'PaymentMethod_Mailed check',
    'PaymentMethod_Credit card (automatic)'
]

def preprocess_input(data: dict) -> pd.DataFrame:
    df = pd.DataFrame([data])

    # ======================
    # MAP GIÁ TRỊ VỀ CSV GỐC
    # ======================

    df['gender_Male'] = 1 if df.loc[0, 'gender'] == 'Nam' else 0
    df['SeniorCitizen'] = 1 if df.loc[0, 'SeniorCitizen'] == 'Có' else 0

    for col in ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']:
        df[f'{col}_Yes'] = 1 if df.loc[0, col] == 'Có' else 0

    # MultipleLines
    df['MultipleLines_Yes'] = 1 if df.loc[0, 'MultipleLines'] == 'Có' else 0
    df['MultipleLines_No phone service'] = 1 if df.loc[0, 'MultipleLines'] == 'Không có DV điện thoại' else 0

    # InternetService
    df['InternetService_Fiber optic'] = 1 if df.loc[0, 'InternetService'] == 'Cáp quang' else 0
    df['InternetService_No'] = 1 if df.loc[0, 'InternetService'] == 'Không sử dụng' else 0

    # Internet sub services
    for col in [
        'OnlineSecurity', 'OnlineBackup',
        'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies'
    ]:
        df[f'{col}_Yes'] = 1 if df.loc[0, col] == 'Có' else 0
        df[f'{col}_No internet service'] = 1 if df.loc[0, col] == 'Không có Internet' else 0

    # Contract
    df['Contract_One year'] = 1 if df.loc[0, 'Contract'] == '1 năm' else 0
    df['Contract_Two year'] = 1 if df.loc[0, 'Contract'] == '2 năm' else 0

    # PaymentMethod – MAP ĐÚNG CSV
    df['PaymentMethod_Electronic check'] = 1 if df.loc[0, 'PaymentMethod'] == 'Hóa đơn điện tử' else 0
    df['PaymentMethod_Mailed check'] = 1 if df.loc[0, 'PaymentMethod'] == 'Hóa đơn bưu điện' else 0
    df['PaymentMethod_Credit card (automatic)'] = 1 if df.loc[0, 'PaymentMethod'] == 'Thẻ tín dụng' else 0

    # Numeric
    df['tenure'] = float(df.loc[0, 'tenure'])
    df['MonthlyCharges'] = float(df.loc[0, 'MonthlyCharges'])
    df['TotalCharges'] = float(df.loc[0, 'TotalCharges'])

    return df[EXPECTED_COLUMNS]
