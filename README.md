
# Proxy management for web scraping

This project is a Scrapy-based web scraper designed to scrape quotes from [quotes.toscrape.com](http://quotes.toscrape.com/) with proxy rotation support using the `scrapy-rotating-proxies` middleware. The proxy rotation helps in avoiding IP bans and throttling by the target website.

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed along with Scrapy. To install Scrapy, use:

```bash
pip install scrapy
```

Additionally, install the `scrapy-rotating-proxies` middleware:

```bash
pip install scrapy-rotating-proxies
```

### Project Structure

```
proxy_rotation/
├── proxy_rotation/
│   ├── __init__.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── quotes_proxy_rotation_spider.py
├── scrapy.cfg
└── README.md
```

### Installing

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/proxy_rotation.git
cd proxy_rotation
```

### Configuration

1. **Proxies Setup:**

   Update the list of proxies in the `settings.py` file:

   ```python
   ROTATING_PROXY_LIST = [
    # if proxy need authentication then list will be in below format
    'http://username:password@proxy1.com:8000',
    # list without authentication
    # 'ip:port'
    'proxy1.com:8000'
    # Add more proxies as needed
   ]
   ```

   - If your proxies require authentication, use the format `http://username:password@proxy:port`.
   - If your proxies do not require authentication, use the format `ip:port`.

2. **Spider Setup:**

   The spider is located in `spiders/quotes_proxy_rotation_spider.py`. It scrapes quotes and author details from the website.

3. **Run the Spider:**

   Run the spider using the following command:

   ```bash
   scrapy crawl quotes_proxy_rotation_spider
   ```

### Features

- **Proxy Rotation:** Uses multiple proxies to avoid IP bans and throttling by rotating through a list of proxies.

- **Robust Scraping:** Handles pagination and extracts detailed information about quotes and authors.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
