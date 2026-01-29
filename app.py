import streamlit as st

# =========================
# CẤU HÌNH TRANG (SỬA ICON TAB)
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

st.sidebar.subheader("📘 Hướng dẫn sử dụng")
st.sidebar.markdown("""
1. Chọn mô hình học máy  
2. Nhập thông tin khách hàng  
3. Nhấn **Dự đoán** để xem kết quả  
""")

# =========================
# TITLE
# =========================
col_title1, col_title2 = st.columns([1, 10])

with col_title1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/1041/1041916.png",
        width=60
    )

with col_title2:
    st.markdown(
        "<h1>DỰ ĐOÁN KHÁCH HÀNG RỜI BỎ DỊCH VỤ</h1>",
        unsafe_allow_html=True
    )

st.markdown("---")

# =========================
# THÔNG TIN KHÁCH HÀNG
# =========================
st.markdown(
    "<div style='background-color:#e8f4fa;padding:15px;border-radius:10px'>"
    "<h3>🧾 Thông tin khách hàng</h3>",
    unsafe_allow_html=True
)

c1, c2, c3, c4, c5 = st.columns(5)

gender = c1.selectbox("Giới tính", ["Nam", "Nữ"])
senior = c2.selectbox("Khách hàng cao tuổi", ["Không", "Có"])
partner = c3.selectbox("Có người thân", ["Không", "Có"])
dependents = c4.selectbox("Có người phụ thuộc", ["Không", "Có"])
tenure = c5.number_input(
    "Thời gian sử dụng (tháng)",
    min_value=0,
    max_value=72,
    step=5,
    value=12
)

c6, c7, c8, c9, c10 = st.columns(5)

phone = c6.selectbox("Dịch vụ điện thoại", ["Có", "Không"])
multiple_lines = c7.selectbox(
    "Nhiều đường dây",
    ["Không", "Có", "Không có DV điện thoại"]
)
internet = c8.selectbox(
    "Internet",
    ["DSL", "Cáp quang", "Không sử dụng"]
)
contract = c9.selectbox(
    "Hợp đồng",
    ["Theo tháng", "1 năm", "2 năm"]
)
paperless = c10.selectbox(
    "Hóa đơn điện tử",
    ["Có", "Không"]
)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("")

# =========================
# DỊCH VỤ GIA TĂNG
# =========================
st.markdown(
    "<div style='background-color:#eaf7ee;padding:15px;border-radius:10px'>"
    "<h3>📡 Dịch vụ gia tăng</h3>",
    unsafe_allow_html=True
)

d1, d2, d3 = st.columns(3)

online_security = d1.selectbox(
    "Bảo mật trực tuyến",
    ["Không", "Có", "Không có Internet"]
)
online_backup = d2.selectbox(
    "Sao lưu trực tuyến",
    ["Không", "Có", "Không có Internet"]
)
device_protection = d3.selectbox(
    "Bảo vệ thiết bị",
    ["Không", "Có", "Không có Internet"]
)

d4, d5, d6 = st.columns(3)

tech_support = d4.selectbox(
    "Hỗ trợ kỹ thuật",
    ["Không", "Có", "Không có Internet"]
)
streaming_tv = d5.selectbox(
    "Truyền hình trực tuyến",
    ["Không", "Có", "Không có Internet"]
)
streaming_movies = d6.selectbox(
    "Phim trực tuyến",
    ["Không", "Có", "Không có Internet"]
)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("")

# =========================
# THANH TOÁN
# =========================
st.markdown(
    "<div style='background-color:#eef3fb;padding:15px;border-radius:10px'>"
    "<h3>💰 Thông tin thanh toán</h3>",
    unsafe_allow_html=True
)

p1, p2, p3 = st.columns(3)

payment_method = p1.selectbox(
    "Hình thức thanh toán",
    [
        "Hóa đơn điện tử",
        "Hóa đơn bưu điện",
        "Chuyển khoản ngân hàng",
        "Thẻ tín dụng"
    ]
)

monthly_charges = p2.number_input(
    "Chi phí hàng tháng",
    min_value=0.0,
    step=10.0,
    value=70.0
)

total_charges = p3.number_input(
    "Tổng chi phí",
    min_value=0.0,
    step=50.0,
    value=1000.0
)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("")

# =========================
# NÚT DỰ ĐOÁN
# =========================
if st.button("🔍 Dự đoán"):
    st.success(f"Đã gửi yêu cầu dự đoán bằng mô hình **{model_name}**")
    st.info("Kết quả dự đoán sẽ được hiển thị khi tích hợp mô hình học máy.")
