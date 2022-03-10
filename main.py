from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route("/list_proof/<listt>")
def list_proof(listt):

    main_list=[1,2,3,4,1,2,5555]
    return render_template('index.html', list=listt, main_list=main_list)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
