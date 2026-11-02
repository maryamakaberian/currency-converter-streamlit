
import streamlit as st

from constant import CURRENCIES
from currency_convertor import get_exchange_rate, convert_crrecny


# Application title and description
st.title(":dollar: Currency Converter")
st.write(
    """This tool allows you to convert amounts between different currencies 🌍.
    Enter an amount and select the currencies to see the result."""
)

# Currency selection (str) and amount input (float)
base_currency = st.selectbox("From Currency (Base):", CURRENCIES, index=1)
target_currency = st.selectbox("To Currency (Target):", CURRENCIES, index=1)
amount = st.number_input("Enter amount:", min_value=0.0, value=100.0)

# Perform conversion only when the inputs are valid
if amount > 0 and base_currency and target_currency:

    # Exchange rate: float or None if the API request fails
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate is not None:
        converted_amount = convert_crrecny(amount, exchange_rate)

        # Display exchange rate and conversion results
        st.success(f"Exchange rate: {exchange_rate:.4f}")

        # Three-column layout: original amount → arrow → converted amount
        col1, col2, col3 = st.columns(3)

        col1.metric(
            label="Base Currency",
            value=f"{amount:.4f} {base_currency}"
        )

        col2.markdown(
            "<h1 style='text-align: center; color: #1685D9;'>➜</h1>",
            unsafe_allow_html=True
        )

        col3.metric(
            label="Target Currency",
            value=f"{converted_amount:.4f} {target_currency}"
        )

    else:
        st.error("Unable to fetch the exchange rate. Please try again later.")

st.markdown("---")
