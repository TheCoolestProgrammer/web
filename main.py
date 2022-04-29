from pathlib import Path

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route("/galery")
def table():
    folder = Path("static/image/mars_images")
    max_folder_id = len(list(folder.iterdir())) - 1
    return render_template('index.html', max_folder_id=max_folder_id)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
