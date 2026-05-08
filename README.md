# Ceneo web scraper

### Summary

An MVP web scraper that collects data from Ceneo.pl, a large price comparison platform. <br>

### What it does

When you run the script, it scrapes a single page (no pagination) and saves the data to a file: results.csv <br>
<br>
Columns: name | rating | reviews | purchased_recently
<br>

### Development

Ceneo.pl uses JavaScript-based pagination on subsequent pages. A planned development is to implement Selenium to enable multi-page scraping.

### Project structure

```bash
Ceneo-scraper
├── config.py # URL and request headers
├── scraper.py # HTTP request, returns BeautifulSoup object
├── parser.py # Extracts product data from HTML
├── utils.py # Data cleaning functions (rating → float, count → int)
├── main.py # Entry point, saves results to CSV
├── requirements.txt
├── wyniki.csv # Output file (git-ignored)
└── logs.txt # Logs sucessfuls saves and errors (git-ignored)
```

### How to run

1. Clone the repository:

```bash
   git clone https://github.com/HadleyApennine/Ceneo-scraper
   cd https://github.com/HadleyApennine/Ceneo-scraper
```

   <br>
2. Create and activate a virtual environment:

```bash
   python -m venv .venv
   .venv\Scripts\activate # Windows
   source .venv/bin/activate # Mac/Linux
```

   <br>
3. Install dependencies:

```bash
   pip install -r requirements.txt
```

   <br>
4. Run the scraper:

```bash
   python main.py
```

   <br>

## Thank you.
