import sqlalchemy
from . import db_session


class Department(db_session.SqlAlchemyBase):
    __tablename__ = 'Department'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    chief = sqlalchemy.Column(sqlalchemy.Integer)
    members = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.id"))
    # или вот такой вариант
    # members = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.Integer), sqlalchemy.ForeignKey("users.id"))
    email = sqlalchemy.Column(sqlalchemy.String)

#     id
#     title (String)
#     chief (Integer)
#     members (list of id`s)
#     email (String)
# #
