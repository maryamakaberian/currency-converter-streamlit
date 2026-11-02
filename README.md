
# 💱 Currency Converter | Python & Streamlit

An interactive currency converter built with **Python** and **Streamlit**, using exchange-rate data from the [Frankfurter API](https://frankfurter.dev/).

This project is part of my hands-on Python learning journey, focusing on API integration, data processing, caching, and building interactive applications.

## ✨ Features

- Convert amounts between supported currencies.
- Retrieve exchange rates from an external API.
- Select source and target currencies using dropdown menus.
- Display exchange rates and converted amounts.
- Cache exchange-rate results for up to three hours using `cachetools`.
- Handle common network and HTTP request errors.
- Provide a simple, interactive Streamlit interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application logic and calculations |
| Streamlit | Interactive web interface |
| Requests | HTTP requests and API integration |
| cachetools | Caching exchange-rate results |
| Frankfurter API | Exchange-rate data |

## 📁 Project Structure

```text
currency-converter-streamlit/
├── src/
│   ├── app.py
│   ├── constant.py
│   └── currency_convertor.py
├── .gitignore
├── README.md
└── requirements.txt
```

### File Descriptions

- **`src/app.py`** — Builds the Streamlit interface and displays conversion results.
- **`src/currency_convertor.py`** — Retrieves exchange rates, handles API requests, and performs currency conversions.
- **`src/constant.py`** — Stores the list of supported currencies.
- **`requirements.txt`** — Lists the required Python packages.
- **`.gitignore`** — Excludes temporary files, Python cache files, and local environments from Git.

## 🚀 Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/maryamakaberian/currency-converter-streamlit.git
cd currency-converter-streamlit
```

### 2. Create a virtual environment

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run src/app.py
```

Streamlit will display a local URL, usually:

http://localhost:8501

Open it in your browser to use the converter.

## ⚙️ How It Works

1. The user selects a base currency and a target currency.
2. The user enters an amount to convert.
3. The application retrieves the exchange rate from the Frankfurter API.
4. The converted amount is calculated using:

   **Converted Amount = Original Amount × Exchange Rate**

5. The result is displayed in the Streamlit interface.

If both currencies are identical, the exchange rate is set to `1.0` without making an API request.

### Caching

The application uses `TTLCache` from `cachetools`:

```python
cache = TTLCache(maxsize=100, ttl=3 * 60 * 60)
```

- **Maximum cache size:** 100 entries.
- **Time to live (TTL):** 3 hours.
- **Purpose:** Reduce repeated API requests for the same currency pair.

The current implementation also caches unsuccessful lookups that return `None`. Improving this behavior is planned for a future version.

## 🌐 API Integration

This application uses the free [Frankfurter API](https://frankfurter.dev/).

Example endpoint:

```text
https://api.frankfurter.dev/v1/latest?base=EUR
```

The API returns exchange rates relative to the selected base currency.

No API key is required.

**Note:** Exchange rates are based on available reference data and are not intended for real-time financial trading.

## 🧠 What I Learned

Through this project, I practiced:

- Writing reusable Python functions with type hints and docstrings.
- Organizing code into separate Python modules.
- Sending HTTP requests using the `requests` library.
- Extracting information from JSON responses and dictionaries.
- Handling exceptions with `try` and `except`.
- Using decorators and caching with `TTLCache`.
- Creating an interactive interface with Streamlit.
- Managing dependencies and organizing a GitHub repository.

## 🔮 Future Improvements

- [ ] Improve error handling and prevent failed API requests from being cached.
- [ ] Add automated tests for currency conversions.
- [ ] Implement a currency-swap button.
- [ ] Add historical exchange-rate charts.
- [ ] Improve the interface and user experience.
- [ ] Deploy the application online.

## 👩‍💻 Author

**Maryam Akaberian**

PhD in Physics | Python, Data Analysis & Machine Learning

## 📌 Project Status

**Version 1.0 — Initial Release**

This is the first version of the project. Future updates will focus on reliability, testing, data visualization, and additional functionality.
