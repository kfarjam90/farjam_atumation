from flask import Flask,request,jsonify,redirect
import string
import random


app = Flask(__name__)

database = {}

def produce_shortcode():
    shortcode = ''
    characters = string.ascii_letters.lower() + string.digits
    for _ in range(6):
        shortcode += random.choice(characters)
    return shortcode

#print(produce_shortcode())

@app.route('/shorten', methods=['POST'])
def shorten_url():
    #{"url": "https://www.example.com/", "shortcode": "asd123"}
    url = request.get_json().get('url')
    shortcode = request.get_json().get('shortcode')

    if not url:
        return jsonify({'error':'URL not present'}),400

    if shortcode:
        if shortcode in database:
            return jsonify({'error': "Shortcode already in use"}),409
        elif len(shortcode) != 6 or not all(characters in string.ascii_letters.lower() + string.digits for characters in shortcode):
            return jsonify({'error':'The provided shortcode is invalid'}),412
    else:
        shortcode = produce_shortcode()

    database[shortcode] = url
  
    return jsonify({'shortcode': shortcode})

@app.route('/<shortcode>')
def redirect_url(shortcode):
    if shortcode not in database:
        return jsonify({"error":"Shortcode not found"}),404
    
    new_url = database[shortcode]

    return redirect(new_url,code=302)


if __name__ == '__main__':
    app.run(debug=True)





