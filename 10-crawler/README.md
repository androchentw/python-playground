# Crawler

* [crawlee-python](https://github.com/apify/crawlee-python)
  * [Alternatives to Scrapy for web scraping in 2024](https://blog.apify.com/alternatives-scrapy-web-scraping/)

## Installation

* [Introduction tutorial](https://crawlee.dev/python/docs/introduction)

```sh
# https://stackoverflow.com/questions/45954528/pip-is-configured-with-locations-that-require-tls-ssl-however-the-ssl-module-in
# brew update && brew upgrade
# brew uninstall --ignore-dependencies openssl; brew install https://github.com/tebelorg/Tump/releases/download/v1.0.0/openssl.rb
# brew install openssl

pip install pyopenssl

pip install 'crawlee[all]'
playwright install

python -c 'import crawlee; print(crawlee.__version__)'

brew install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
```

## Create and run project from template

```sh
pipx --help
brew install poetry

# suitable for static page
pipx run crawlee create crawler-beautifulsoup
# alternative: crawlee create crawler-beautifulsoup
cd crawler-beautifulsoup
poetry install
poetry run python -m crawler-beautifulsoup

# suitable for dynamic content
pipx run crawlee create crawler-playwright
# alternative: crawlee create crawler-playwright
cd crawler-playwright
poetry install
poetry run python -m crawler-playwright
```

```text
[crawlee.beautifulsoup_crawler._beautifulsoup_crawler] INFO  Final request statistics:
┌───────────────────────────────┬───────────┐
│ requests_finished             │ 52        │
│ requests_failed               │ 0         │
│ retry_histogram               │ [52]      │
│ request_avg_failed_duration   │ None      │
│ request_avg_finished_duration │ 0.710651  │
│ requests_finished_per_minute  │ 192       │
│ requests_failed_per_minute    │ 0         │
│ request_total_duration        │ 36.953843 │
│ requests_total                │ 52        │
│ crawler_runtime               │ 16.22249  │
└───────────────────────────────┴───────────┘
```

```text
[crawlee.playwright_crawler._playwright_crawler] INFO  Final request statistics:
┌───────────────────────────────┬─────────────┐
│ requests_finished             │ 64          │
│ requests_failed               │ 0           │
│ retry_histogram               │ [64]        │
│ request_avg_failed_duration   │ None        │
│ request_avg_finished_duration │ 19.349865   │
│ requests_finished_per_minute  │ 26          │
│ requests_failed_per_minute    │ 0           │
│ request_total_duration        │ 1238.391384 │
│ requests_total                │ 64          │
│ crawler_runtime               │ 148.122176  │
└───────────────────────────────┴─────────────┘
```