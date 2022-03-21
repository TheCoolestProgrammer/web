from flask import render_template
from flask import Flask
from data import db_session
from data.jobs import Jobs

db_session.global_init("db/blogs.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route("/")
def index():

    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()

    return render_template("index.html", jobs=jobs)
def main():
    job = Jobs()
    job.team_leader = "captain Jack Sparrow"
    job.job = "pirating"
    job.work_size = 24
    job.collaborators = "Tobie Mckguire, Batman, Ryan Gosling"
    job.is_finished =False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    job = Jobs()
    job.team_leader = "Leon from brawl stars"
    job.job = "bank robbery"
    job.work_size = 2
    job.collaborators = "Frank, deadpool, terminator"
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    job = Jobs()
    job.team_leader = "russian"
    job.job = "aneckdot(need american)"
    job.work_size = 128
    job.collaborators = "german"
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
