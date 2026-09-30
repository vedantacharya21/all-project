# 💱 Currency Converter

A simple and user-friendly **Currency Converter web application** built with **Python and Streamlit**. It allows users to convert an amount from one currency to another using the latest available exchange rates.

Link:

## 🚀 Features

* 💱 Convert between multiple currencies
* 🌐 Uses live exchange-rate data
* 💰 Enter any amount for conversion
* 🔄 Select source and target currencies
* 📊 Displays the converted amount
* 📈 Displays the current exchange rate
* ⚠️ Handles API and internet connection errors
* 📱 Responsive Streamlit interface

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Requests**
* **Frankfurter API**

## 📂 Project Structure

```text
Currency-Converter/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/vedantacharya21/currency-converter.git
```

### 2. Open the project folder

```bash
cd currency-converter
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Run the following command:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 💡 How It Works

1. Enter the amount you want to convert.
2. Select the currency you are converting **from**.
3. Select the currency you want to convert **to**.
4. Click the **Convert** button.
5. The application fetches the latest exchange-rate information.
6. The converted amount and exchange rate are displayed.

### Example

```text
100 USD → INR

100 USD = 8,xxx.xx INR
1 USD = xx.xx INR
```

The actual value depends on the exchange rate returned by the API.

## 🌐 API

This project uses the **Frankfurter API** to retrieve exchange-rate information.

API endpoint:

```text
https://api.frankfurter.app/latest
```

No API key is required for the basic usage implemented in this project.

## 📋 Supported Currencies

The current version supports:

* 🇺🇸 USD — US Dollar
* 🇮🇳 INR — Indian Rupee
* 🇪🇺 EUR — Euro
* 🇬🇧 GBP — British Pound
* 🇯🇵 JPY — Japanese Yen
* 🇦🇺 AUD — Australian Dollar
* 🇨🇦 CAD — Canadian Dollar
* 🇨🇭 CHF — Swiss Franc
* 🇨🇳 CNY — Chinese Yuan
* 🇦🇪 AED — UAE Dirham

## ⚠️ Error Handling

The application handles:

* Internet connection problems
* API request failures
* Invalid API responses
* Unexpected errors

## 🚀 Deployment

This Streamlit application can be deployed on platforms such as:

* Streamlit Community Cloud
* Render
* Other platforms that support Python/Streamlit applications

For deployment, make sure `requirements.txt` is included in the repository.

## 🔮 Future Improvements

Possible improvements include:

* 🔄 Add a currency swap button
* 🌎 Support more currencies
* 📅 Add historical exchange rates
* 📊 Add exchange-rate charts
* 💾 Cache exchange rates
* 🕒 Display the last updated time
* 🎨 Improve the UI with custom styling
* 📱 Improve mobile responsiveness
* 📈 Add historical currency trends

## 👨‍💻 Author

**Vedant Acharya**

Computer Engineering Student

## 📄 License

This project is open-source and available for educational and personal use.
