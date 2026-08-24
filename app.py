import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Grade Checker",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Grade Checker")
st.write("Enter your marks to check your grade.")

st.divider()

# User Input
marks = st.number_input(
    "Enter Your Marks",
    min_value=0.0,
    max_value=100.0,
    step=0.1
)

# Button
if st.button("Check Grade"):

    if 90 <= marks <= 100:
        grade = "A1"
    elif 80 <= marks < 90:
        grade = "A2"
    elif 70 <= marks < 80:
        grade = "B1"
    elif 60 <= marks < 70:
        grade = "B2"
    elif 50 <= marks < 60:
        grade = "C1"
    elif 40 <= marks < 50:
        grade = "C2"
    elif 33 <= marks < 40:
        grade = "D"
    elif 21 <= marks < 33:
        grade = "E1"
    else:
        grade = "E2"

    st.success(f"🎉 Your Grade is: **{grade}**")