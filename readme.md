# 🔐 OTP Generator

A simple and secure **OTP (One-Time Password) Generator** built using Python and Streamlit.

The application generates a random 6-digit OTP and allows the user to verify it. Each OTP is valid for **5 minutes**.

Link:

## 🚀 Features

* 🔢 Generate a random 6-digit OTP
* 🔐 Uses Python's `secrets` module for secure random generation
* ⏳ OTP validity of 5 minutes
* ✅ OTP verification
* ❌ Invalid OTP detection
* ⏰ Expired OTP detection
* 🔄 Generate a new OTP after expiration
* 🖥️ Simple and user-friendly Streamlit interface

## 🛠️ Technologies Used

* Python
* Streamlit
* Secrets
* Time

## 📁 Project Structure

```text
OTP-Generator/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/vedantacharya21/otp-generator.git
```

### 2. Open the project folder

```bash
cd otp-generator
```

### 3. Install the required package

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Run the Streamlit application using:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🔄 How It Works

1. Click **Generate OTP**.
2. The application generates a random 6-digit OTP.
3. The OTP is stored temporarily in the Streamlit session.
4. The OTP remains valid for **5 minutes**.
5. Enter the generated OTP in the input field.
6. Click **Verify OTP**.
7. If the OTP matches and has not expired, verification is successful.
8. If the OTP is incorrect, an error message is displayed.
9. After 5 minutes, the OTP expires and a new OTP must be generated.

## 🔐 Security

This project uses Python's `secrets` module instead of the `random` module for OTP generation.

The `secrets` module is designed for generating random values suitable for security-sensitive applications.

> **Note:** This is an educational project. In a real authentication system, OTPs should normally be sent through a secure channel such as email or SMS rather than displayed directly on the screen.

## 📌 Future Improvements

Possible improvements include:

* 📧 Send OTP through email
* 📱 Send OTP through SMS
* ⏱️ Add a live countdown timer
* 🚫 Limit the number of verification attempts
* 🔄 Add a "Resend OTP" feature
* 🔒 Hash OTPs before storing them
* 👤 Add user authentication
* 📊 Add OTP verification logs

## 👨‍💻 Author

**Vedant Acharya**

## 📄 License

This project is open-source and available for educational purposes.
