import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

st.title("⚖️ BMI Calculator")
st.write("Calculate your BMI and check whether your weight is in the healthy range.")

st.divider()

# User Inputs
weight = st.number_input(
    "Enter Your Weight (kg)",
    min_value=0.0,
    format="%.1f"
)

height_cm = st.number_input(
    "Enter Your Height (cm)",
    min_value=0.0,
    format="%.1f"
)

if st.button("Calculate BMI"):

    if weight <= 0:
        st.error("Weight must be greater than 0 kg.")
    elif height_cm <= 0:
        st.error("Height must be greater than 0 cm.")
    else:
        height = height_cm / 100

        bmi = weight / (height ** 2)

        st.subheader("Your Result")

        st.metric("BMI", f"{bmi:.2f}")

        # BMI Category
        if bmi < 18.5:
            category = "Underweight"
            color = "🟡"
        elif bmi < 25:
            category = "Normal Weight"
            color = "🟢"
        elif bmi < 30:
            category = "Overweight"
            color = "🟠"
        else:
            category = "Obese"
            color = "🔴"

        st.write(f"### {color} {category}")

        # Healthy Weight Range
        min_weight = 18.5 * (height ** 2)
        max_weight = 24.9 * (height ** 2)

        st.subheader("Healthy Weight Range")
        st.write(f"**{min_weight:.1f} kg - {max_weight:.1f} kg**")

        # Gain / Lose Weight
        st.subheader("Recommendation")

        if weight < min_weight:
            gain = min_weight - weight
            st.warning(f"You should gain approximately **{gain:.1f} kg**.")
        elif weight > max_weight:
            lose = weight - max_weight
            st.warning(f"You should lose approximately **{lose:.1f} kg**.")
        else:
            st.success("🎉 Congratulations! Your weight is within the healthy range.")

        # BMI Progress Bar
        progress = min(bmi / 40, 1.0)
        st.subheader("BMI Scale")
        st.progress(progress)

        # BMI Table
        st.subheader("BMI Categories")

        st.table({
            "Category": [
                "Underweight",
                "Normal Weight",
                "Overweight",
                "Obese"
            ],
            "BMI Range": [
                "< 18.5",
                "18.5 - 24.9",
                "25 - 29.9",
                "30+"
            ]
        })