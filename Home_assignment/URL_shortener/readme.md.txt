# Flask URL Shortener

This is a simple URL shortener implemented using Flask, a micro web framework for Python.

## Introduction

This application allows users to shorten long URLs into shorter, more manageable URLs. It generates a shortcode for each URL provided by the user, making it easier to share and remember.

## Features

- Shorten long URLs into shorter, more manageable ones.
- Generate a random shortcode for each URL or allow custom shortcodes.
- Redirect users to the original URL when accessing the shortcode.

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

To shorten a URL, send a POST request to `/shorten` with a JSON payload containing the URL you want to shorten. Optionally, you can provide a custom shortcode. If you don't provide a shortcode, a random one will be generated.

Example:

```bash
{
    "url": "https://www.example.com/"
}