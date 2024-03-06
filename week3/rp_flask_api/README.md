# Flask Application with Connexion

This is a simple Flask application integrated with Connexion for handling API requests defined in a Swagger specification.

## Prerequisites

Ensure you have Python and Flask installed.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python <filename>.py
    ```

2. Access the application in your web browser or through API requests.

## Description

The provided Python script integrates Flask with Connexion to create a web application that serves API requests defined in the Swagger specification file (`swagger.yml`).

- The `connexion` module is imported to create an instance of the Connexion application.
- The `render_template` function from `flask` is imported to render HTML templates.
- An instance of `connexion.App` is created with the specification directory set to `"./"` (current directory).
- The Swagger API specification is added using the `add_api` method, which loads the specification from the file `swagger.yml`.
- A route for the root URL (`"/"`) is defined using the `@app.route` decorator, which renders the `home.html` template using the `render_template` function.
- The main block ensures that the application runs when executed directly (`__name__ == "__main__"`), with the host set to `"0.0.0.0"`, port set to `8000`, and debug mode enabled (`debug=True`).

## Files

- `swagger.yml`: Swagger API specification file defining the API endpoints and operations.
- `home.html`: HTML template file for the home page.

## License

[MIT License](LICENSE)
