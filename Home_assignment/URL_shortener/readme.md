# Flask URL Shortener

## Introduction

This is a simple Flask application that provides a URL shortening service. It allows users to create short URLs for long URLs and retrieve statistics for each short URL.

## Features

- Shortening URLs: Users can send a POST request to /shorten with a JSON payload containing the long URL to be shortened. If a custom shortcode is provided, it will be used; otherwise, a random shortcode will be generated.
- Redirection: Users can use the generated shortcodes to access the original long URLs. Accessing /`<shortcode>` will redirect users to the original URL.
- Statistics: Users can retrieve statistics for a shortened URL by accessing /`<shortcode>`/stats. Statistics include creation time, last redirect time, and the number of

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.x
- Flask
- [db.py](db.py) module containing the `database` dictionary

## Installation

1. Clone or download the repository to your local machine.
2. Install Flask using pip:

   ```bash
   pip install Flask
   ```
3. Ensure the `db.py` module is present in the same directory as `app.py`.
4. Run the `app.py` file using Python:

   ```bash
   python app.py
   ```

## Usage

### Shortening URLs

To shorten a URL, send a POST request to /shorten endpoint with the following JSON payload

Example:

```bash
{
    "url": "https://www.example.com/"
}
```
