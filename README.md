# Ceneo web scraper

### Summary

An MVP web scraper that collects data from Ceneo.pl, a large price comparison platform.

### What it does

When you run the script, it scrapes a single page (no pagination) and saves the data to a file results.csv <br>
name | rating | reviews | purchesed_recently

### Development

Ceneo.pl uses JavaScript-based pagination on subsequent pages. A planned developtment is to implement Selenium to enable multi-page scraping.

### Project structure

Ceneo-scraper <br>
├── config.py # URL and request headers <br>
├── scraper.py # HTTP request, returns BeautifulSoup object <br>
├── parser.py # Extracts product data from HTML <br>
├── utils.py # Data cleaning functions (rating → float, count → int) <br>
├── main.py # Entry point, saves results to CSV <br>
├── requirements.txt <br>
├── wyniki.csv # Output file (git-ignored) <br>
└── logs.txt # Logs sucessfuls saves and errors (git-ignored) <br>

### How to run

1. Clone the repository: <br>
   git clone https://github.com/HadleyApennine/Ceneo-scraper
   cd https://github.com/HadleyApennine/Ceneo-scraper
   <br>
2. Create and activate a virtual environment: <br>
   python -m venv .venv
   .venv\Scripts\activate # Windows
   source .venv/bin/activate # Mac/Linux
   <br>
3. Install dependencies: <br>
   pip install -r requirements.txt
   <br>
4. Run the scraper: <br>
   python main.py
   <br>

## Thank you.
