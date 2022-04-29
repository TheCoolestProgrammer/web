from pathlib import Path

from flask import Flask, render_template, request
from flask_wtf import file

app = Flask(__name__)

@app.route('/')
@app.route("/galery", methods=['POST', 'GET'])
def table():
    folder = Path("static/image/mars_images")
    max_folder_id = len(list(folder.iterdir()))
    if request.method == 'POST':
        file = request.files["file"]
        file.save(f"static/image/mars_images/mars{max_folder_id+1}.png")
        max_folder_id +=1
    return render_template('index.html', max_folder_id=max_folder_id)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
