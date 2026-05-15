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

Dockerfile file was put inside repo - on the same level as main.py <br>

1. Build the Docker image:

```bash
   docker build -t python-scraper .
```

   <br>
2. Run the container (basic):

```bash
   docker run --rm python-scraper
```

   <br>
3. Run interactively (for debugging) - it runs the script and put you inside the docker command line:

```bash
   docker run --rm -it python-scraper /bin/bash

```

   <br>
4.  in case there would be some folder sharing it - for example to put results.csv file outside container it would look like that (not tested by me, but tough demonstration how to do folder sharing between host and container):

```bash
   docker run -v HOST-DIRECTORY:/CONTAINER-DIRECTORY:rw --rm python-scraper

```

   <br>

## Thank you.
