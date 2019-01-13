from datetime import datetime, timedelta, date
from flask_wtf import FlaskForm as Form
from wtforms import StringField, SelectField, DateField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError


def check_client_priority_choice(f, d):
    if not d:
        raise ValidationError("Select valid Client Priority.")


def check_target_date(f, data):
    tomm = datetime.now().date() + timedelta(days=1)
    d = f.target_date.data
    try:
        if (d-tomm) < timedelta(days=0):
            raise ValidationError("Target Date should be greater than Today 's date.")
    except Exception as e:
        pass


class FrequestForm(Form):
    title = StringField("Title", validators=[InputRequired("Title is required"),
                                             Length(min=5, max=20,
                                                    message="Title should be more than 5 characters and less 20")])
    description = StringField("Description", validators=[])
    client = SelectField("Client", choices=None, validators=[])
    client_priority = SelectField("Client Priority", default=0, choices=None,
                                  validators=[]#check_client_priority_choice]
                                 )
    target_date = DateField("Target Date", format="%d-%m-%Y",
                            validators=[InputRequired("Target date for feature is required"),
                                        check_target_date],
                            render_kw={'placeholder': 'dd-mm-yyyy'})
    product_area = SelectField("Product Area", choices=[('policies','Policies'),
                                                        ('billing','Billing'),
                                                        ('claims', 'Claims'),
                                                        ('reports', 'Reports')])


class ClientForm(Form):
    client_name = StringField("Client Name", validators=[InputRequired("Client name is required"),
                                                    Length(min=1, message="Minimum 1 character is client name accepted")])

    priority = IntegerField("Max Priorities", validators=[], default=100)
