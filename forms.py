from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, EmailField, TextAreaField
from wtforms.validators import DataRequired


class CafeForm(FlaskForm):
    name = StringField("Name of Cafe", validators=[DataRequired()])
    map_url = StringField("Google Map Link to Cafe", validators=[DataRequired()])
    img_url = StringField("Image URL of Cafe", validators=[DataRequired()])
    location = StringField("Location of Cafe", validators=[DataRequired()])
    seats = IntegerField("Number of Seats", validators=[DataRequired()])
    toilet = BooleanField("Has Toilets?", validators=[DataRequired()])
    wifi = BooleanField("Has Wi-Fi?", validators=[DataRequired()])
    sockets = BooleanField("Has Sockets?", validators=[DataRequired()])
    calls = BooleanField("Able to Call Cafe?", validators=[DataRequired()])
    price = StringField("Price of Coffee? (with currency)", validators=[DataRequired()])
    submit = SubmitField("Add Cafe", validators=[DataRequired()])

    def to_dict(self):
        return


class SearchForm(FlaskForm):
    search = StringField('Search Cafe', validators=[DataRequired()], render_kw={"placeholder": "Search By City", "class": "form-control me-2 fs-5"})
    submit = SubmitField('Search', render_kw={"class": "btn btn-outline-dark fs-5 fw-bold"})


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    phone = IntegerField("Phone Number", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message", validators=[DataRequired()])
