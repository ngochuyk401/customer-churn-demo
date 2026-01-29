import streamlit as st

st.set_page_config(
    page_title="Hệ thống cảnh báo khách hàng rời bỏ dịch vụ",
    layout="wide"
)

st.title("📊 HỆ THỐNG CẢNH BÁO SỚM KHÁCH HÀNG RỜI BỎ DỊCH VỤ")

st.markdown(
    """
    Ứng dụng demo hỗ trợ nhà quản lý dự đoán nguy cơ khách hàng rời bỏ dịch vụ 
    dựa trên các mô hình học máy.
    """
)

# SIDEBAR - CHỌN MÔ HÌNH

st.sidebar.header("⚙️ Cấu hình dự đoán")

model_name = st.sidebar.selectbox(
    "Chọn mô hình học máy",
    ["KNN", "SVM", "Random Forest"]
)

st.sidebar.info(
    f"Mô hình đang được chọn: **{model_name}**"
)

# FORM NHẬP THÔNG TIN

st.header("🧾 Nhập thông tin khách hàng")

col1, col2, col3 = st.columns(3)

with col1:
    gender_vi = st.selectbox("Giới tính", ["Nam", "Nữ"])
    senior_vi = st.selectbox("Khách hàng cao tuổi", ["Không", "Có"])
    partner_vi = st.selectbox("Có người thân đi kèm", ["Không", "Có"])
    dependents_vi = st.selectbox("Có người phụ thuộc", ["Không", "Có"])

with col2:
    tenure = st.number_input(
        "Thời gian sử dụng dịch vụ (tháng)",
        min_value=0,
        max_value=100,
        value=12
    )
    phone_service_vi = st.selectbox("Sử dụng dịch vụ điện thoại", ["Không", "Có"])
    multiple_lines_vi = st.selectbox("Nhiều đường dây", ["Không", "Có"])

with col3:
    internet_service = st.selectbox(
        "Dịch vụ Internet",
        ["DSL", "Cáp quang", "Không sử dụng"]
    )
    contract = st.selectbox(
        "Loại hợp đồng",
        ["Theo tháng", "1 năm", "2 năm"]
    )
    payment_method = st.selectbox(
        "Hình thức thanh toán",
        [
            "Hóa đơn điện tử",
            "Hóa đơn gửi bưu điện",
            "Chuyển khoản ngân hàng",
            "Thẻ tín dụng"
        ]
    )

monthly_charges = st.number_input(
    "Chi phí hàng tháng",
    min_value=0.0,
    value=70.0
)

total_charges = st.number_input(
    "Tổng chi phí",
    min_value=0.0,
    value=1000.0
)

# NÚT DỰ ĐOÁN

st.markdown("---")

if st.button("🔍 DỰ ĐOÁN NGUY CƠ RỜI BỎ"):
    st.subheader("📌 Thông tin đã nhập")

    # Map tiếng Việt -> giá trị gốc
    input_data = {
        "gender": "Male" if gender_vi == "Nam" else "Female",
        "SeniorCitizen": 1 if senior_vi == "Có" else 0,
        "Partner": "Yes" if partner_vi == "Có" else "No",
        "Dependents": "Yes" if dependents_vi == "Có" else "No",
        "tenure": tenure,
        "PhoneService": "Yes" if phone_service_vi == "Có" else "No",
        "MultipleLines": "Yes" if multiple_lines_vi == "Có" else "No",
        "InternetService": (
            "No" if internet_service == "Không sử dụng" else internet_service
        ),
        "Contract": {
            "Theo tháng": "Month-to-month",
            "1 năm": "One year",
            "2 năm": "Two year"
        }[contract],
        "PaymentMethod": {
            "Hóa đơn điện tử": "Electronic check",
            "Hóa đơn gửi bưu điện": "Mailed check",
            "Chuyển khoản ngân hàng": "Bank transfer (automatic)",
            "Thẻ tín dụng": "Credit card (automatic)"
        }[payment_method],
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    st.json(input_data)

    st.success(
        f"Yêu cầu dự đoán đã được gửi bằng mô hình **{model_name}** "
        "(chức năng dự đoán sẽ được tích hợp ở bước tiếp theo)."
    )
