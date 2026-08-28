# ⚖️ BMI Calculator

A simple and interactive BMI (Body Mass Index) Calculator built using **Python** and **Streamlit**.

Users can enter their weight and height to calculate their BMI, view their health category, healthy weight range, and receive personalized recommendations.

---

Link:

## 🚀 Features

- Calculate BMI instantly
- Displays BMI value
- Identifies BMI category
  - 🟡 Underweight
  - 🟢 Normal Weight
  - 🟠 Overweight
  - 🔴 Obese
- Shows healthy weight range
- Weight gain/loss recommendation
- BMI progress bar
- BMI category reference table
- Input validation for invalid values
- Clean and responsive Streamlit interface

---

## 📂 Project Structure

```
BMI-Calculator/
│
├── app.py
├── requirements.txt
├── README.md
```

---

## 🛠️ Technologies Used

- Python 3.10+
- Streamlit

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/vedantacharya21/bmi-calculator.git
```

### 2. Navigate to the project

```bash
cd bmi-calculator
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

If the above command doesn't work, use:

```bash
python -m streamlit run app.py
```

---

## 📊 BMI Classification

| Category | BMI Range |
|----------|-----------|
| Underweight | Below 18.5 |
| Normal Weight | 18.5 – 24.9 |
| Overweight | 25.0 – 29.9 |
| Obese | 30.0 and above |

---

## 📸 Preview

The application includes:

- Weight input
- Height input
- BMI calculation
- Healthy weight range
- Personalized recommendation
- BMI progress indicator
- BMI classification table

---

## 💡 Formula Used

BMI is calculated using:

```
BMI = Weight (kg) / Height² (m²)
```

Example:

```
Weight = 70 kg
Height = 1.75 m

BMI = 70 / (1.75 × 1.75)
BMI = 22.86
```

---

## 🎯 Future Improvements

- Imperial unit support (Feet/Inches & Pounds)
- BMI gauge chart
- Health tips based on BMI
- Dark mode support
- Download BMI report as PDF
- BMI history tracking
- Age and gender-based recommendations

---

## 👨‍💻 Author

**Vedant Acharya**

---

## 📄 License

This project is licensed under the MIT License.