import streamlit as st

st.set_page_config(
    page_title="CGPA/SPI to Percentage Calculator",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 CGPA / SPI to Percentage Calculator")
st.write("Convert your CGPA or SPI into percentage.")

st.divider()

choice = st.selectbox(
    "Choose Your Choice",
    [
        "CGPA to Percentage",
        "SPI to Percentage"
    ]
)

value = st.number_input(
    f"Enter {choice.split()[0]}",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.01,
    format="%.2f"
)

if st.button("Calculate Percentage"):
    percentage = value * 9.5

    st.success(f"Percentage: {percentage:.2f}%")

st.divider()

st.info("Note: The conversion formula used is Percentage = CGPA/SPI × 9.5.")