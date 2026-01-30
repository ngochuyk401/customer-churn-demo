import streamlit as st
import pandas as pd
from preprocessing.preprocess import preprocess_input
from models.model_loader import load_model

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Dự đoán khách hàng rời bỏ dịch vụ",
    page_icon="📡",
    layout="wide"
)

# =========================
# SIDEBAR
# =========================
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3059/3059446.png",
    width=120
)

st.sidebar.subheader("⚙️ Chọn mô hình")

model_name = st.sidebar.selectbox(
    "",
    ["KNN", "SVM", "Random Forest"]
)

st.sidebar.markdown("---")

st.sidebar.subheader("📘 Hướng dẫn")
st.sidebar.markdown("""
1. Chọn mô hình  
2. Nhập thông tin khách hàng  
3. Nhấn **Dự đoán**  
""")

# =========================
# TITLE
# =========================
st.markdown(
    "<h1 style='text-align:center'>📊 DỰ ĐOÁN KHÁCH HÀNG RỜI BỎ DỊCH VỤ</h1>",
    unsafe_allow_html=True
)
st.markdown("---")

# =========================
# THÔNG TIN KHÁCH HÀNG
# =========================
st.subheader("🧾 Thông tin khách hàng")

c1, c2, c3, c4, c5 = st.columns(5)

gender = c1.selectbox("Giới tính", ["Male", "Female"])
senior = c2.selectbox("Khách hàng cao tuổi", [0, 1])
partner = c3.selectbox("Có người thân", ["Yes", "No"])
dependents = c4.selectbox("Có người phụ thuộc", ["Yes", "No"])
tenure = c5.number_input("Thời gian sử dụng (tháng)", 0, 72, 1)

c6, c7, c8, c9, c10 = st.columns(5)

phone = c6.selectbox("Dịch vụ điện thoại", ["Yes", "No"])
multiple_lines = c7.selectbox(
    "Nhiều đường dây",
    ["Yes", "No", "No phone service"]
)
internet = c8.selectbox(
    "Internet",
    ["DSL", "Fiber optic", "No"]
)
contract = c9.selectbox(
    "Hợp đồng",
    ["Month-to-month", "One year", "Two year"]
)
paperless = c10.selectbox(
    "Hóa đơn điện tử",
    ["Yes", "No"]
)

# =========================
# DỊCH VỤ GIA TĂNG
# =========================
st.subheader("📡 Dịch vụ Internet")

d1, d2, d3 = st.columns(3)

online_security = d1.selectbox(
    "Bảo mật trực tuyến",
    ["Yes", "No", "No internet service"]
)
online_backup = d2.selectbox(
    "Sao lưu trực tuyến",
    ["Yes", "No", "No internet service"]
)
device_protection = d3.selectbox(
    "Bảo vệ thiết bị",
    ["Yes", "No", "No internet service"]
)

d4, d5, d6 = st.columns(3)

tech_support = d4.selectbox(
    "Hỗ trợ kỹ thuật",
    ["Yes", "No", "No internet service"]
)
streaming_tv = d5.selectbox(
    "Truyền hình trực tuyến",
    ["Yes", "No", "No internet service"]
)
streaming_movies = d6.selectbox(
    "Phim trực tuyến",
    ["Yes", "No", "No internet service"]
)

# =========================
# THANH TOÁN
# =========================
st.subheader("💰 Thanh toán")

p1, p2, p3 = st.columns(3)

payment_method = p1.selectbox(
    "Hình thức thanh toán",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = p2.number_input(
    "Chi phí hàng tháng",
    min_value=0.0,
    step=5.0,
    value=70.0
)

total_charges = p3.number_input(
    "Tổng chi phí",
    min_value=0.0,
    step=50.0,
    value=100.0
)

st.markdown("---")

# =========================
# DỰ ĐOÁN
# =========================
if st.button("🔍 Dự đoán"):

    # =========================
    # 1. Gom dữ liệu đầu vào
    # =========================
    input_data = {
        'gender': gender,
        'SeniorCitizen': senior,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone,
        'MultipleLines': multiple_lines,
        'InternetService': internet,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': paperless,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }

    # =========================
    # 2. Hiển thị dữ liệu nhập
    # =========================
    with st.expander("🧾 Dữ liệu đã nhập"):
        st.dataframe(pd.DataFrame([input_data]))

    # =========================
    # 3. Tiền xử lý
    # =========================
    processed_df = preprocess_input(input_data)

    with st.expander("📄 Dữ liệu sau tiền xử lý"):
        st.dataframe(processed_df)

    # =========================
    # 4. Load model & predict
    # =========================
    model = load_model(model_name)
    prediction = model.predict(processed_df)[0]

    # =========================
    # 5. Kết quả
    # =========================
    st.subheader("📊 Kết quả")

    if prediction == 1:
        st.error("⚠️ Khách hàng **CÓ NGUY CƠ RỜI BỎ** dịch vụ")
        st.markdown("""
        **Khuyến nghị:**
        - Cung cấp ưu đãi giá
        - Nâng cao hỗ trợ kỹ thuật
        - Chăm sóc khách hàng chủ động
        """)
    else:
        st.success("✅ Khách hàng **KHÔNG có nguy cơ rời bỏ**")
        st.markdown("""
        **Khuyến nghị:**
        - Duy trì chất lượng dịch vụ
        - Tiếp tục chính sách hiện tại
        """)
