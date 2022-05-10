from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db, User, Inventory, Warehouse

from jinja2 import StrictUndefined
import webbrowser
import requests
import json 
from pprint import pprint

app = Flask(__name__, static_url_path='/static') 
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def welcome_page():
    """Show the Welcome page"""

    return render_template("homepage.html")


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""
    email = request.form.get("email")
    password = request.form.get("password")

    if email == "" or password == "":
        flash ("Not a valid email/password combination.")
    else:
        user_exist = User.query.filter_by(email=email).first()

        if user_exist:
            flash ("This email is already registered on our website. Please log in.")
        else:
            user = User(email=email, password=password)
            db.session.add(user)
            db.session.commit()
            flash ("Account created! Please log in.")
    
    return redirect ("/")


@app.route("/login", methods=["POST"])
def log_in():
    """Existing user log in."""
    
    email = request.form.get("email")
    password = request.form.get("password")
    
    user = User.query.filter_by(email=email).first()
    
    if not user or user.password != password:
        flash("Your input does not match our records. Please try again.")

    else:
        session["user"] = user.id
        flash(f"Welcome, {user.email}!")
        return redirect("/user_homepage")
   
    return redirect("/")


@app.route("/logout")
def logout():
    """User must be logged in."""
    
    if "user" in session:
        del session["user"]
        flash("Logged Out.")
    return redirect("/")


@app.route("/user_homepage")
def user_homepage():
    """Asks what you'd like to do."""

    return render_template("user_homepage.html")


@app.route("/create_inventory", methods=["POST"])
def create_inventory():
    """Allows user to create a new inventory item"""
    
    upc = request.form.get("upc")
    name = request.form.get("name")
    quantity = request.form.get("quantity")

    new_product = Inventory(upc=upc, name=name, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()
           
    return 


@app.route("/create_warehouse", methods=["POST"])
def create_inventory():
    """Allows user to create a new warehouse location"""
    
    location = request.form.get("location")

    warehouse_location = Warehouse(location=name)
    db.session.add(warehouse_location)
    db.session.commit()
           
    return 


@app.route("/inventory_warehouse", methods=["POST"])
def inventory_warehouse():
    """Allows user to assign inventory to warehouse location"""
    
    warehouse_name = 
    product_name = 
    product_quantity = 

    obj = InventoryWarehouse(warehouse_name=warehouse_name, product_name=product_name, product_quantity=product_quantity)
    db.session.add(obj)
    db.session.commit()
           
    return 






if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)