from flask import Flask,request,jsonify,redirect
from db import database,stats
import string
import random
import json
from datetime import datetime

app = Flask(__name__)

def produce_shortcod():
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
    #{"url": "https://www.example.com/", "shortcode": "asd123"}
    url = request.get_json().get('url')
    shortcode = request.get_json().get('shortcode')

    if not url:
        return jsonify({'error':"Url not present"}),400
    
    if shortcode:
        if shortcode in database:
            return jsonify({'error':'Shortcode already in use'}),409
        elif len(shortcode) != 6 or not all(characters in string.ascii_letters.lower() + string.digits for characters in shortcode):
            return jsonify({'error':'The procide shorcode in in valid'}),412
        
    else:
        shortcode = produce_shortcod()

    database[shortcode] = url
    stats[shortcode] = {
        'created': datetime.now().strftime(("%Y-%m-%dT%H:%M:%S.%fZ")),
        'lastRedirect': None,
        'redirectCount': 0
    }

    with open('urls.json','w') as file:
        json.dump(database,file)

    return jsonify({'shortcode':shortcode})


@app.route('/<shortcode>')
def redirect_url(shortcode):
    """
    Redirect to the URL associated with the provided shortcode.

    Returns:
    response: A redirection response to the URL associated with the shortcode, or an error response if the shortcode is not found.
    """
    if shortcode not in database:
        return jsonify({'error':'Shortcode not found'}),404
    
    new_url = database[shortcode]
    stats[shortcode]['lastRedirect'] = datetime.now().strftime(("%Y-%m-%dT%H:%M:%S.%fZ"))
    stats[shortcode]['redirectCount'] += 1

    return redirect(new_url,302)

@app.route('/<shortcode>/stats')
def get_stats(shortcode):
    """
    Retrieve statistics for the URL associated with the provided shortcode.

    Returns:
    response: A JSON response containing statistics for the URL associated with the shortcode, or an error response if the shortcode is not found.

    """
    #{"created": "2017-05-10T20:45:00.000Z", "lastRedirect": "2018-05-16T10:16:24.666Z", "redirectCount": 5}

    if shortcode not in database:
        return jsonify({'error':'shortcode not found'}),404

    url_stats = stats[shortcode]
    return jsonify({
        'created': url_stats['created'],
        'lastRedirect': url_stats['lastRedirect'],
        'redirectCount': url_stats['redirectCount']
    })

if __name__ == '__main__':
    app.run(debug=True)
