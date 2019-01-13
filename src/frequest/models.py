from .__init__ import app
from flask_sqlalchemy import SQLAlchemy

app.db = SQLAlchemy(app)

class Frequest(app.db.Model):
    __tablename__ = "frequest"
    title = app.db.Column(app.db.String(20), primary_key=True)
    description = app.db.Column(app.db.String(100), index=True)
    client = app.db.Column(app.db.String(40), app.db.ForeignKey('client.client'))
    target_date = app.db.Column(app.db.String(11))
    client_priority = app.db.Column(app.db.Integer())
    product_area = app.db.Column(app.db.String(10))

    def __repr__(self):
        return '<Feature Request %r>' % self.title


class Client(app.db.Model):
    __tablename__ = "client"
    client = app.db.Column(app.db.String(40), primary_key=True)
    priority = app.db.Column(app.db.Integer())

    def __repr__(self):
        return '<Client %r>' % self.client