# URL Shortener API

This API allows users to shorten URLs and track redirection statistics.

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

## Usage

1. Start the server by running:
    ```
    python app.py
    ```

2. The server will start running locally at http://127.0.0.1:5000/.

### API Endpoints

1. **Shorten URL:**
   - **Endpoint:** `POST /shorten`
   - **Request Body:** JSON object with keys 'url' and optional 'shortcode'.
   - **Response:** JSON response containing the shortcode for the shortened URL.

2. **Redirect URL:**
   - **Endpoint:** `GET /<shortcode>`
   - **Response:** Redirection to the original URL associated with the provided shortcode.

3. **Get Stats:**
   - **Endpoint:** `GET /<shortcode>/stats`
   - **Response:** JSON response containing statistics for the URL associated with the shortcode.

## Testing

Use tools like Postman or cURL to send requests to the API endpoints and verify the responses.

1. **Test the /shorten endpoint:**
   - set the request URL to http://localhost:5000/shorten
   - go to the body tab, select raw and choose JSON as the format.
   - Enter a JSON object with the url key and the URL you want to shorten.
```json
{
    "url": "https://www.example.com/"
}


### Request Body




