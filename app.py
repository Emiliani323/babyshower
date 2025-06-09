from flask import Flask, render_template, request, redirect, flash
import os
from database import init_db, get_all_gifts, reserve_gift

app = Flask(__name__, static_folder='static')
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key')

# Initialize DB when app starts
with app.app_context():
    init_db()

@app.route("/")
def index():
    error = request.args.get('error')
    if error == 'already_reserved':
        flash('This gift was already reserved. Please choose another.', 'error')
    return render_template("index.html", gifts=get_all_gifts())

@app.route("/reserve", methods=["POST"])
def reserve():
    name = request.form.get("name", "").strip()
    gift_id = request.form.get("gift_id")
    
    if not name or not gift_id:
        flash('Please enter your name and select a gift', 'error')
        return redirect("/")
    
    if reserve_gift(int(gift_id), name):
        flash(f'Thank you {name}! Gift reserved successfully.', 'success')
    else:
        return redirect("/?error=already_reserved")
    
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))