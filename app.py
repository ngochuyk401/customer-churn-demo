import streamlit as st
from preprocessing.preprocess import preprocess_input


def interpret_result(prob):
    if prob < 0.3:
        level = "Thấp"
        message = "Khách hàng có xu hướng tiếp tục sử dụng dịch vụ."
        advice = "Không cần can thiệp ngay, tiếp tục duy trì chất lượng dịch vụ."
        color = "green"
    elif prob < 0.6:
        level = "Trung bình"
        message = "Khách hàng có dấu hiệu cân nhắc rời bỏ dịch vụ."
        advice = "Nên theo dõi và chủ động chăm sóc, tư vấn gói dịch vụ phù hợp."
        color = "orange"
    else:
        level = "Cao"
        message = "Khách hàng có nguy cơ rời bỏ dịch vụ cao."
        advice = "Cần có biện pháp giữ chân như ưu đãi, hỗ trợ kỹ thuật hoặc chăm sóc đặc biệt."
        color = "red"

    return level, message, advice, color

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
    # 2. Hiển thị dữ liệu đã nhập (đối chiếu)
    # =========================
    with st.expander("🧾 Thông tin khách hàng đã nhập"):
        st.dataframe(pd.DataFrame([input_data]))

    # =========================
    # 3. Tiền xử lý
    # =========================
    processed_df = preprocess_input(input_data)

    with st.expander("📄 Dữ liệu sau tiền xử lý (đầu vào của mô hình)"):
        st.dataframe(processed_df)

    # =========================
    # 4. Load mô hình & dự đoán
    # =========================
    model = load_model(selected_model)
    prediction = model.predict(processed_df)[0]

    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(processed_df)[0][1]
    else:
        prob = None

    # =========================
    # 5. Hiển thị kết quả
    # =========================
    st.subheader("📊 Kết quả dự đoán")

    if prob is not None:
        level, message, advice, color = interpret_result(prob)

        if color == "green":
            st.success(f"🟢 Mức độ rủi ro: {level}")
        elif color == "orange":
            st.warning(f"🟡 Mức độ rủi ro: {level}")
        else:
            st.error(f"🔴 Mức độ rủi ro: {level}")

        st.write(f"**Xác suất rời bỏ dịch vụ:** {prob:.2%}")
        st.write(f"**Nhận định:** {message}")
        st.write(f"**Khuyến nghị:** {advice}")
    else:
        if prediction == 1:
            st.error("⚠️ Khách hàng có nguy cơ rời bỏ dịch vụ")
        else:
            st.success("✅ Khách hàng không có nguy cơ rời bỏ dịch vụ")



