from data import db_session, new_api
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(new_api.blueprint)
    app.run()

if __name__=="__main__":
    main()