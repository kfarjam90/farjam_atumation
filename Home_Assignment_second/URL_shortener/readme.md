# URL Shortening Service with Flask and SQLAlchemy

This is a Flask web application that provides a URL shortening service. It allows users to create short URLs, redirect to the original long URLs associated with the short URLs, and retrieve statistics for each short URL. The application uses SQLAlchemy to interact with a SQLite database for storing and retrieving the URLs and their statistics.


## Installation

1. Install Flask and SQLAlchemy using pip:

   ```
   pip install Flask SQLAlchemy
   ```
2. Clone the repository and navigate to the project directory:

   ```
   git clone https://github.com/kfarjam90/url-shortener.git
   cd url-shortener
   ```


## Models

### URL

The URL model represents a short URL and its associated long URL.

- `id` (Integer): The primary key for the URL.
- `shortcode` (String): The unique 6-character code representing the short URL.
- `url` (String): The original long URL.

### Stats

The Stats model stores statistics for each short URL, such as the creation date, last redirect date, and redirect count.

- `id` (Integer): The primary key for the stats.
- `shortcode` (String): The unique 6-character code representing the short URL.
- `created` (DateTime): The date and time when the short URL was created.
- `last_redirect` (DateTime): The date and time of the last redirection to the long URL.
- `redirect_count` (Integer): The number of times the short URL has been redirected.

### API Endpoints

1. **Shorten URL:**

   This endpoint is used to shorten a URL.

   - **Endpoint:** `POST /shorten`
   - **Request Body:** JSON object with keys 'url' and optional 'shortcode'.
   - **Response:** JSON response containing the shortcode for the shortened URL.
2. **Redirect URL:**

   This endpoint redirects the user to the long URL associated with the provided shortcode.

   - **Endpoint:** `GET /<shortcode>`
   - **Response:** Redirection to the original URL associated with the provided shortcode.
3. **Get Stats:**

   This endpoint retrieves the statistics for the short URL associated with the provided shortcode.

   - **Endpoint:** `GET /<shortcode>/stats`
   - **Response:** JSON response containing statistics for the URL associated with the shortcode.

## Usage

1. Install the required dependencies: `flask` and `sqlalchemy`.
2. Run the Flask application: `python app.py`.
3. Use a tool like postman to interact with the URL shortening service.

## Testing

Use tools like Postman to send requests to the API endpoints and verify the responses.

1. **To test the `/shorten` endpoint:**
   - Set the request method to `POST`.
   - Set the request URL to `http://localhost:5000/shorten`.
   - Go to the `body` tab, select `raw` and choose `JSON` as the format.
   - Enter a JSON object with the url key and the URL you want to shorten.
   - You can also include a `shortcode` key if you want.
   - Click send `send` to send the request.

```json
{
    "url": "https://www.example.com/"
}
```

Response:

```json
{
    "shortcode": "produce_shortcode"
}
```

2. **To test the `/<shortencode>` endpoint:**

   - Set the request method to `GET`.
   - Set the request URL to `http://localhost:5000/<shortencode>`, replacing `/<shortencode>` with the shortcode you received from the `/shorten`          endpint.
   - Click send `send` to send the request. You should be redirected to the orgiginal URL associetd with the shortcode.
3. **To test the `/<shortencode>/stats` endpoint:**

   - Set the request method to `GET`.
   - Set the request URL to `http://localhost:5000/<shortencode>/stats`, replacing `/<shortencode>` with the shortcode you received from the `/shorten`          endpint.
   - Click send `send` to send the request. You should receive a JSON response with statistics for the URL associated with the shortcode.

Response:

```json
{
    "created": "2017-05-10T20:45:00.000Z",
    "lastRedirect": "2018-05-16T10:16:24.666Z",
    "redirectCount": 2
}
```
