from flask import Flask, render_template
import json
from data import db_session

db_session.global_init("db/blogs.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    app.run()



if __name__ == '__main__':
    main()
