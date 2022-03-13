from flask import Flask, render_template
import json
app = Flask(__name__)


@app.route('/')
@app.route("/member")
def table():
    with open("templates/members.json", "rt", encoding="utf8") as f:
        names_list = json.loads(f.read())
    return render_template('index.html',members=names_list)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
