from inspect import stack
import json
from flask import request, render_template, flash, redirect, url_for
from .__init__ import app
from .models import Client, Frequest
from .forms import ClientForm, FrequestForm

btrace = lambda: stack()[1][3]


def add_row(f):
    app.db.session.add(f)
    app.db.session.commit()


def get_priority(client=None):
    if client:
        c = Client.query.filter_by(client=client).first()
        if c and c.priority:
            p = [i for i in range(1, c.priority + 1)]
            for i in Frequest.query.filter_by(client=client):
                if i.client_priority in p:
                    p.remote(i.client_priority)
            return p

    return [i for i in range(1, 101)]



@app.route("/clientpriority",  methods=['GET'])
def client_priority():
    client = request.args.get('client')
    return json.dumps(get_priority(client))


def select_choices(form):
    clients = Client.query.all()
    form.client.choices = [(i.client, i.client) for i in clients]
    priority = get_priority(form.client.data or None)
    if not priority:
        flash("ERROR: Client have already requested Maximum no of Feature request")
    form.client_priority.choices = [(str(i), int(i)) for i in priority] or [("", 0)]


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def frequest():
    form = FrequestForm()
    select_choices(form)

    if request.method == 'POST' and form.validate_on_submit():
        if form.title.data in [i.title for i in Frequest.query.all()]:
            flash("ERROR: Feature Request with title name  '{}' is already present".format(form.title.data))
            form = FrequestForm()
            select_choices(form)
        else:
            c = Client.query.filter_by(client=form.client.data).first()
            try:
                if not c.priority:
                    c.priority = int(form.client_priority.data)
                    app.db.session.commit()
                f = Frequest(title=form.title.data,
                         description=form.description.data,
                         client=form.client.data,
                         target_date=form.target_date.data,
                         product_area=form.product_area.data)
                add_row(f)
                flash("Successfully Registered Feature Request with title '{}'".format(form.title.data))
                priority = get_priority(form.client.data)
                form.client_priority.choices = [(str(i), int(i)) for i in priority]

            except Exception as e:
                flash("ERROR: Failed to update Feature Request {}".format(str(e)))
    if not form.client.choices:
        flash("ERROR: No Client is present. Add a new client First.")
        return redirect(url_for('client'))

    return render_template('frequest.html', form=form)


@app.route('/client', methods=['GET', 'POST'])
def client():
    form = ClientForm()
    if request.method == 'POST' and form.validate_on_submit():
        if form.client_name.data in [i.client for i in Client.query.all()]:
            flash("ERROR: Client with name '{}' is already present".format(form.client_name.data))
            form = ClientForm()
        else:
            client = Client(client=str(form.client_name.data), priority=0)
            add_row(client)
            flash("Successfully Update Client with name '{}'".format(form.client_name.data))

    return render_template('client.html', form=form)
