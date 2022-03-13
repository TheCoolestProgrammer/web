from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route("/table/<sex>/<int:age>")
def table(sex,age):

    return render_template('index.html',sex=sex,age=age)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
