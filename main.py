from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title):
    param = {}
    param["title"] = title
    return render_template('index.html', **param)

@app.route("/training/<prof>")
def training(prof):
    return render_template('trainings.html', prof=prof.lower())
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
