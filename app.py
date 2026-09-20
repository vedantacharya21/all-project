import streamlit as st
import requests

st.set_page_config(
    page_title="Currency Converter",
    page_icon="💱",
    layout="centered"
)

st.title("💱 Currency Converter")
st.write("Convert currencies using the latest exchange rates.")

# Currency list
currencies = {
    "USD": "US Dollar",
    "INR": "Indian Rupee",
    "EUR": "Euro",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "AED": "UAE Dirham"
}

# Input
amount = st.number_input(
    "Enter amount",
    min_value=0.01,
    value=100.0,
    step=1.0
)

col1, col2 = st.columns(2)

with col1:
    from_currency = st.selectbox(
        "From",
        list(currencies.keys()),
        format_func=lambda x: f"{x} - {currencies[x]}"
    )

with col2:
    to_currency = st.selectbox(
        "To",
        list(currencies.keys()),
        index=1,
        format_func=lambda x: f"{x} - {currencies[x]}"
    )

if st.button("Convert 💱", use_container_width=True):

    if from_currency == to_currency:
        result = amount
        rate = 1

    else:
        try:
            url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()

                result = data["rates"][to_currency]

                # Get exchange rate for 1 unit
                rate_url = (
                    f"https://api.frankfurter.app/latest"
                    f"?amount=1&from={from_currency}&to={to_currency}"
                )

                rate_response = requests.get(rate_url, timeout=10)
                rate_data = rate_response.json()

                rate = rate_data["rates"][to_currency]

            else:
                st.error("Unable to fetch exchange rate.")

        except requests.exceptions.RequestException:
            st.error("Internet connection or API error.")

        except Exception as e:
            st.error(f"Something went wrong: {e}")

    # Display result
    st.success(
        f"{amount:,.2f} {from_currency} = "
        f"{result:,.2f} {to_currency}"
    )

    st.info(
        f"1 {from_currency} = {rate:.4f} {to_currency}"
    )