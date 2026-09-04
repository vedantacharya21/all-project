import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="centered")

st.title("📏 Unit Converter")
st.write("Convert common units quickly and easily.")

# -----------------------------
# Conversion Data
# -----------------------------
length_units = {
    "Meter": 1,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Millimeter": 0.001
}

weight_units = {
    "Kilogram": 1,
    "Gram": 0.001,
    "Milligram": 0.000001,
    "Pound": 0.453592
}

time_units = {
    "Second": 1,
    "Minute": 60,
    "Hour": 3600,
    "Day": 86400
}

category = st.selectbox(
    "Select Category",
    ["Length", "Weight", "Temperature", "Time"]
)

value = st.number_input("Enter Value", value=1.0)

# -----------------------------
# LENGTH
# -----------------------------
if category == "Length":

    from_unit = st.selectbox("From", list(length_units.keys()))
    to_unit = st.selectbox("To", list(length_units.keys()))

    result = value * length_units[from_unit] / length_units[to_unit]

    st.success(f"Result: {result:.4f} {to_unit}")

# -----------------------------
# WEIGHT
# -----------------------------
elif category == "Weight":

    from_unit = st.selectbox("From", list(weight_units.keys()))
    to_unit = st.selectbox("To", list(weight_units.keys()))

    result = value * weight_units[from_unit] / weight_units[to_unit]

    st.success(f"Result: {result:.4f} {to_unit}")

# -----------------------------
# TIME
# -----------------------------
elif category == "Time":

    from_unit = st.selectbox("From", list(time_units.keys()))
    to_unit = st.selectbox("To", list(time_units.keys()))

    result = value * time_units[from_unit] / time_units[to_unit]

    st.success(f"Result: {result:.4f} {to_unit}")

# -----------------------------
# TEMPERATURE
# -----------------------------
elif category == "Temperature":

    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]

    from_unit = st.selectbox("From", temp_units)
    to_unit = st.selectbox("To", temp_units)

    if from_unit == to_unit:
        result = value

    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32

    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9

    elif from_unit == "Celsius" and to_unit == "Kelvin":
        result = value + 273.15

    elif from_unit == "Kelvin" and to_unit == "Celsius":
        result = value - 273.15

    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        result = (value - 32) * 5/9 + 273.15

    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        result = (value - 273.15) * 9/5 + 32

    st.success(f"Result: {result:.2f} {to_unit}")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")