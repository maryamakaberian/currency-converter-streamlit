
import requests
from cachetools import cached, TTLCache

# Cache up to 100 results, each valid for 3 hours (TTL in seconds).
cache = TTLCache(maxsize=100, ttl=3 * 60 * 60)


@cached(cache)
def get_exchange_rate(base_currency: str, target_currency: str) -> float | None:
    """Retrieve the exchange rate between two currencies."""

    # No conversion is needed when both currencies are identical.
    if base_currency == target_currency:
        return 1.0

    url = f"https://api.frankfurter.dev/v1/latest?base={base_currency}"

    try:
        # Send an HTTP GET request with a 10-second timeout.
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Extract exchange rates from the JSON response (dictionary).
        rates = response.json().get("rates", {})
        return rates.get(target_currency)

    except requests.exceptions.RequestException:
        # Return None if the API request fails.
        return None


def convert_crrecny(amount: float, exchange_rate: float) -> float:
    """Convert an amount using the given exchange rate."""
    return amount * exchange_rate


if __name__ == "__main__":
    # Run this section only when executing this file directly.
    base_currency = input("Enter base currency: ")
    target_currency = input("Enter target currency: ")
    amount = float(input("Enter amount: "))

    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = convert_crrecny(amount, exchange_rate)

    print(f"{amount} {base_currency} is {converted_amount:.2f} {target_currency}")
