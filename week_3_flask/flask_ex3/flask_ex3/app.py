from flask import Flask, render_template, redirect, url_for, request, Response,send_from_directory,jsonify
import pandas as pd
import os
import uuid
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'parham' and password == 'farjam':
            return 'success'
        else:
            return 'failed'

@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or file.content_type == "application/vnd.ms-excel":
        df = pd.read_excel(file)
        return df.to_html()

@app.route(rule='/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']

    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    )

    return response

@app.route(rule='/convert_csv_two', methods=['POST'])
def convert_csv_two():
    file = request.files['file']

    df = pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads',filename))

    return render_template('download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads',filename,download_name = 'result.csv')



if __name__ == "__main__":
    app.run(debug=True)
