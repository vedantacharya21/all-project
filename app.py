import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Age Calculator",
    page_icon="🎂",
    layout="centered"
)

st.title("🎂 Age Calculator")

birth_date = st.date_input(
    "Select your Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

if st.button("Calculate Age"):

    today = date.today()

    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    st.success(f"🎉 Your Age is **{age} Years**")