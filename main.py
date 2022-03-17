from flask import Flask, render_template
import json
from data import db_session
from data.users import User

db_session.global_init("db/blogs.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    #app.run()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Spike"
    user.surname = "Shpigel"
    user.age = 21
    user.position = "head hunter"
    user.speciality = "striker"
    user.address = "somewhere on bebop"
    user.email = "see_ya_space_cowboy@syndicat.net"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Jett"
    user.surname = "Black"
    user.age = 52
    user.position = "head hunter"
    user.speciality = "technic"
    user.address = "on the kitchen"
    user.email = "i_willnt_save_your_ass_anymore@univerce_police.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Fai"
    user.surname = "Valentine"
    user.age = 20
    user.position = "head hunter"
    user.speciality = "striker"
    user.address = "somewhere in casino"
    user.email = "pls_give_me_some_money@gmail.com"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Edward"
    user.age = 11
    user.position = "i hacked this database LMAO ^W^"
    user.speciality = "hacker 0_0"
    user.address = "2-0934-0213o"
    user.email = "-------------@------.---"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Einstein"
    user.name = "Corgie"
    user.age = 1000000
    user.position = "corgie"
    user.speciality = "corgie"
    user.address = "corgie"
    user.email = "corgie@corgie.corgie"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
