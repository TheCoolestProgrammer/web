from flask import Flask
from sqlalchemy import func

name = input()
global_init(name)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    # app.run()

    db_sess = create_session()
    counter = []
    for user in db_sess.query(Jobs):
        counter.append(len(user.collaborators.split()))
    maxx = max(counter)
    for user in db_sess.query(Jobs):
        if len(user.collaborators.split()) == maxx:
            print(User[user.team_leader])

    # for user in user.query(User).all():
    #     print(user)


if __name__ == '__main__':
    main()
