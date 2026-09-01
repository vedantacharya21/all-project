# 🎓 CGPA / SPI to Percentage Calculator

A simple and user-friendly **CGPA/SPI to Percentage Calculator** built using Python and Streamlit.

This application allows students to convert their **CGPA or SPI into percentage** using a simple conversion formula.

Link:

## 🚀 Features

* CGPA to Percentage conversion
* SPI to Percentage conversion
* Input validation between 0 and 10
* Percentage displayed up to 2 decimal places
* Simple and clean user interface
* Built with Streamlit

## 🧮 Formula

The application uses the following formula:

```text
Percentage = CGPA/SPI × 9.5
```

### Example

If your CGPA is `8.5`:

```text
8.5 × 9.5 = 80.75%
```

> **Important:** The conversion formula can vary depending on the university or educational board. Verify the applicable formula before using the result for official purposes.

## 🛠️ Technologies Used

* Python
* Streamlit

## 📂 Project Structure

```text
CGPA-SPI-Calculator/
│
├── app.py
├── requirements.txt
└── README.md
```

## 💻 Run the Project Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/vedantacharya21/cgpa-spi-calculator.git
```

### Step 2: Open the project folder

```bash
cd cgpa-spi-calculator
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 📌 Future Improvements

* Add Percentage to CGPA conversion
* Add university-specific conversion formulas
* Add semester-wise SPI calculation
* Add overall CGPA calculation
* Add calculation history
* Improve UI and customization

## 👨‍💻 Author

**Vedant Acharya**

## 📄 License

This project is open-source and available for educational purposes.
