from flask import Flask

name = input()
global_init(name)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    # app.run()

    db_sess = create_session()
    counter = []
    ids = []
    for user in db_sess.query(Jobs):
        counter.append(len(user.collaborators.split()))
    maxx = max(counter)
    for user in db_sess.query(Jobs):
        if len(user.collaborators.split()) == maxx:
            ids.append(user.team_leader)
    another_list = []
    for i in ids:
        a = db_sess.query(User).get(i)
        b = a.name + " " + a.surname
        if b not in another_list:
            another_list.append(b)
    for i in another_list:
        print(i)


if __name__ == '__main__':
    main()
