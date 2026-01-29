import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Dự đoán khách hàng rời bỏ dịch vụ",
    layout="wide"
)

# =========================
# LOGO (FPT / TELCO)
# =========================
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/5/5c/FPT_logo_2010.svg",
    width=180
)

st.markdown(
    "<h1 style='text-align: center;'>DỰ ĐOÁN KHÁCH HÀNG RỜI BỎ DỊCH VỤ</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Hệ thống demo ứng dụng học máy trong cảnh báo sớm customer churn</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# =========================
# CHỌN MÔ HÌNH
# =========================
st.subheader("⚙️ Lựa chọn mô hình học máy")

model_name = st.radio(
    "",
    ["KNN", "SVM", "Random Forest"],
    horizontal=True
)

st.markdown("---")

# =========================
# THÔNG TIN KHÁCH HÀNG
# =========================
st.subheader("🧾 Thông tin khách hàng")

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
        max_value=120,
        step=5,
        value=12
    )
    phone_vi = st.selectbox("Sử dụng dịch vụ điện thoại", ["Có", "Không"])
    multi_vi = st.selectbox("Nhiều đường dây", ["Không", "Có"])

with col3:
    internet = st.selectbox(
        "Dịch vụ Internet",
        ["DSL", "Cáp quang", "Không sử dụng"]
    )
    contract = st.selectbox(
        "Loại hợp đồng",
        ["Theo tháng", "1 năm", "2 năm"]
    )
    paperless_vi = st.selectbox("Hóa đơn điện tử", ["Có", "Không"])

# =========================
# DỊCH VỤ BỔ SUNG
# =========================
st.subheader("📡 Dịch vụ gia tăng")

col4, col5, col6 = st.columns(3)

with col4:
    online_security = st.selectbox("Bảo mật trực tuyến", ["Không", "Có"])
    online_backup = st.selectbox("Sao lưu trực tuyến", ["Không", "Có"])

with col5:
    device_protection = st.selectbox("Bảo vệ thiết bị", ["Không", "Có"])
    tech_support = st.selectbox("Hỗ trợ kỹ thuật", ["Không", "Có"])

with col6:
    streaming_tv = st.selectbox("Truyền hình trực tuyến", ["Không", "Có"])
    streaming_movies = st.selectbox("Phim trực tuyến", ["Không", "Có"])

# =========================
# THANH TOÁN
# =========================
st.subheader("💰 Thông tin thanh toán")

col7, col8 = st.columns(2)

with col7:
    payment_method = st.selectbox(
        "Hình thức thanh toán",
        [
            "Hóa đơn điện tử",
            "Hóa đơn gửi bưu điện",
            "Chuyển khoản ngân hàng",
            "Thẻ tín dụng"
        ]
    )

with col8:
    monthly_charges = st.number_input(
        "Chi phí hàng tháng",
        min_value=0.0,
        step=10.0,
        value=70.0
    )
    total_charges = st.number_input(
        "Tổng chi phí",
        min_value=0.0,
        step=50.0,
        value=1000.0
    )

# =========================
# NÚT DỰ ĐOÁN
# =========================
st.markdown("---")

if st.button("🔍 DỰ ĐOÁN NGUY CƠ RỜI BỎ", use_container_width=True):
    st.success(f"Yêu cầu dự đoán đã được gửi bằng mô hình **{model_name}**")
    st.info("Chức năng dự đoán sẽ được tích hợp mô hình học máy ở bước tiếp theo.")
