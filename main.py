from flask import Flask, url_for, redirect, render_template, request
from forms import *
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

bootstrap = Bootstrap5()
bootstrap.init_app(app)


@app.route("/", methods=["GET", "POST"])
def home():
    search = SearchForm()
    cafes = requests.get(url="https://rest-cafe-pj0t.onrender.com/all").json()['cafes']
    if search.submit.data and search.data:
        cafes = requests.get(url=f"https://rest-cafe-pj0t.onrender.com/search?loc={search.search.data}").json()
        return render_template('search.html', cafes=cafes)
    return render_template("index.html", cafes=cafes, page_title="Coffe and Wifi", search=search)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    search = SearchForm()
    form = CafeForm()
    if search.submit.data and search.data and search.validate_on_submit():
        cafes = requests.get(url=f"https://rest-cafe-pj0t.onrender.com/search?loc={search.search.data}").json()
        return render_template('search.html', cafes=cafes, search=search)
    if form.submit.data and form.data and form.validate_on_submit():
        data = {
            "name": form.name.data,
            "map_url": form.map_url.data,
            "img_url": form.img_url.data,
            "seats": form.seats.data,
            "toilet": form.toilet.data,
            "wifi": form.wifi.data,
            "sockets": form.sockets.data,
            "calls": form.calls.data,
            "price": form.price.data,
            "location": form.location.data
        }
        test = requests.post(url="https://rest-cafe-pj0t.onrender.com/add", data=data)
        print(test)
        return redirect(url_for('home'))
    return render_template("add.html", form=form, page_title="Add Cafe", search=search)


@app.route("/list_cafes", methods=["GET", "POST"])
def list_cafes():
    search = SearchForm()
    if search.submit.data and search.data:
        cafes = requests.get(url=f"https://rest-cafe-pj0t.onrender.com/search?loc={search.search.data}").json()
        return render_template('search.html', cafes=cafes, search=search)
    return render_template('search.html', search=search)


@app.route("/cafe/<int:number>")
def cafe_details(number):
    search = SearchForm()
    if search.submit.data and search.data:
        cafes = requests.get(url=f"https://rest-cafe-pj0t.onrender.com/search?loc={search.search.data}").json()
        return render_template('search.html', cafes=cafes)
    cafes = requests.get(url="https://rest-cafe-pj0t.onrender.com/all").json()['cafes']
    cafe = cafes[number - 1]
    return render_template("details.html", cafe=cafe, search=search)


@app.route('/contact', methods=["GET", "POST"])
def contact_us():
    search = SearchForm()
    contact = ContactForm()
    if search.submit.data and search.data:
        return redirect(url_for('list_cafes'))
    if contact.validate_on_submit():
        pass
    return render_template("contact.html", search=search, contact=contact)


if __name__ == "__main__":
    app.run(debug=True)
