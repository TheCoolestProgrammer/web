import flask
from flask import render_template, jsonify

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs/<int:job_id>')
def get_news(job_id):

    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'news':
                [item.to_dict(only=('id', 'job', 'team_leader'))
                 for item in jobs if item.id == job_id]
        }
    )