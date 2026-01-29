import streamlit as st

st.set_page_config(page_title="Churn Prediction Demo")

st.title("Hệ thống cảnh báo khách hàng rời bỏ dịch vụ")

st.header("Nhập thông tin khách hàng")

gender = st.selectbox(
    "Giới tính",
    ["Male", "Female"]
)

tenure = st.number_input(
    "Thời gian sử dụng dịch vụ (tháng)",
    min_value=0,
    max_value=100,
    value=12
)

contract = st.selectbox(
    "Loại hợp đồng",
    ["Month-to-month", "One year", "Two year"]
)

payment_method = st.selectbox(
    "Hình thức thanh toán",
    ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]
)

monthly_charges = st.number_input(
    "Chi phí hàng tháng",
    min_value=0.0,
    value=70.0
)

if st.button("Xác nhận thông tin"):
    st.subheader("Dữ liệu đã nhập")
    st.write({
        "Giới tính": gender,
        "Thời gian sử dụng": tenure,
        "Hợp đồng": contract,
        "Thanh toán": payment_method,
        "Chi phí hàng tháng": monthly_charges
    })
