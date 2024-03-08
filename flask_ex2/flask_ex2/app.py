from flask import Flask, render_template,redirect,url_for


app = Flask(__name__)


@app.route("/")
def index():
    mylist = [1,2,3,4,5]
    return render_template("index.html" ,mylist=mylist)

@app.route('/other')
def other():
    some_text = 'hello world'
    return render_template('other.html',some_text=some_text)

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, time= 2):
    return s * time

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

if __name__ == "__main__":
    app.run(debug=True)