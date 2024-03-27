from flask import Flask, request, jsonify, redirect
import string
import random
from datetime import datetime
from models import Session, URL, Stats

app = Flask(__name__)


def produce_shortcode():
    """
    Generate a random shortcode consisting of 6 characters.

    Returns:
    str: A randomly generated shortcode composed of lowercase letters (a-z) and digits (0-9).

    """
    shortcode = ''
    characters = string.ascii_letters.lower() + string.digits
    for _ in range(6):
        shortcode += random.choice(characters)
    return shortcode


@app.route('/shorten', methods=['POST'])
def shorten_url():
    """
    Shorten a URL by generating a unique shortcode.
    This function expects a JSON object with keys 'url' and 'shortcode' in the request body.

    Returns:
    JSON: A JSON response containing the shortcode for the shortened URL.
    """
    # {"url": "https://www.example.com/", "shortcode": "asd123"}
    url = request.get_json().get('url')
    shortcode = request.get_json().get('shortcode')

    session = Session()

    if not url:
        return jsonify({'error': "Url not present"}), 400

    if shortcode:
        existing_url = session.query(URL).filter_by(shortcode=shortcode).first()

        if existing_url:
            return jsonify({'error': 'Shortcode already in use'}), 409
        elif len(shortcode) != 6 or not all(char in string.ascii_letters.lower() + string.digits for char in shortcode):
            return jsonify({'error': 'The provided shortcode is invalid'}), 412

    else:
        shortcode = produce_shortcode()
        existing_url = session.query(URL).filter_by(shortcode=shortcode).first()

    new_url = URL(shortcode=shortcode, url=url)
    new_stats = Stats(shortcode=shortcode, created=datetime.now())
    session.add(new_url)
    session.add(new_stats)
    session.commit()
    session.close()

    return jsonify({'shortcode': shortcode}), 201


@app.route('/<shortcode>')
def redirect_url(shortcode):
    """
    Redirect to the URL associated with the provided shortcode.

    Returns:
    response: A redirection response to the URL associated with the shortcode, or an error response if the shortcode is not found.
    """
    session = Session()
    url = session.query(URL).filter_by(shortcode=shortcode).first()
    session.refresh(url)

    if not url:
        return jsonify({'error': 'Shortcode not found'}), 404

    stats = session.query(Stats).filter_by(shortcode=shortcode).first()
    stats.last_redirect = datetime.now()
    stats.redirect_count += 1
    session.commit()
    session.refresh(url)
    session.close()
    return redirect(url.url, 302)


@app.route('/<shortcode>/stats')
def get_stats(shortcode):
    """
    Retrieve statistics for the URL associated with the provided shortcode.

    Returns:
    response: A JSON response containing statistics for the URL associated with the shortcode, or an error response if the shortcode is not found.

    """
    # {"created": "2017-05-10T20:45:00.000Z", "lastRedirect": "2018-05-16T10:16:24.666Z", "redirectCount": 5}
    session = Session()
    stats = session.query(Stats).filter_by(shortcode=shortcode).first()

    if not stats:
        return jsonify({'error': 'Shortcode not found'}), 404

    response = {
        'created': stats.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'lastRedirect': stats.last_redirect.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'redirectCount': stats.redirect_count
    }

    session.close()

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)