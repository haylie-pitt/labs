# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from apod_model import get_apod_data, is_valid_date
from datetime import date

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages

@app.route("/")
def home():
    try:
        apod_data = get_apod_data()
        return render_template("index.html", apod_data=apod_data, current_date=date.today())
    except Exception as e:
        flash(str(e))
        return render_template("index.html", apod_data=None)

@app.route("/history", methods=["GET", "POST"])
def history():
    if request.method == "POST":
        selected_date = request.form.get("date")
        try:
            if selected_date and is_Fvalid_date(date.fromisoformat(selected_date)):
                apod_data = get_apod_data(selected_date)
                return render_template("history.html", apod_data=apod_data, selected_date=selected_date)
            else:
                flash("Invalid date. Please select a date from June 16, 1995, to today.")
                return redirect(url_for("history"))
        except Exception as e:
            flash(str(e))
            return redirect(url_for("history"))
    return render_template("history.html", apod_data=None)
