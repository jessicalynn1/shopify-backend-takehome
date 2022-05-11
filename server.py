from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db, Inventory, Warehouse, InventoryWarehouse

from jinja2 import StrictUndefined
import webbrowser
# import requests
import json 
from pprint import pprint

app = Flask(__name__, static_url_path='/static') 
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route("/homepage")
def homepage():
    """Asks what you'd like to do."""

    return render_template("homepage.html")


@app.route("/create_inventory", methods=["POST"])
def create_inventory():
    """Allows user to create a new inventory item"""
    
    product_code = request.form.get("product-code")
    name = request.form.get("name")
    description = request.form.get("name")
    quantity = request.form.get("quantity")
    warehouse_name = request.form.get("")
    #create drop down menu to pick warehouse

    new_product = Inventory(product_code=product_code, name=name, description=description, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()
           
    return render_template("homepage.html")


@app.route("/edit_inventory", methods=["POST"])
def edit_inventory():
    """Allows user to edit an existing inventory item"""
    
    #query the inventory table to get item
    #get new input/data that needs to be changed from form
    #send inventory item back to database with changes

    edited = Inventory(product_code=product_code, name=name, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()
           
    return render_template("homepage.html")


@app.route("/delete_inventory", methods=["POST"])
def delete_inventory():
    """Allows user to delete an existing inventory item"""
    
    # get item from form that user submits
    #query the inventory table to get item
    db.session.delete(item)
    db.session.commit()

           
    return render_template("homepage.html")


@app.route("/create_warehouse", methods=["POST"])
def create_warehouse():
    """Allows user to create a new warehouse location"""
    
    location = request.form.get("location")
    db_location = Warehouse.query.filter_by(name=location).first()

    if not db_location:
        warehouse_location = Warehouse(name=location)
        db.session.add(warehouse_location)
        db.session.commit()
    else:
        # flash msg "Sorry this warehouse location already exists."

        return render_template("homepage.html")


@app.route("/inventory_warehouse", methods=["POST"])
def inventory_warehouse():
    """Allows user to assign inventory to warehouse location"""
    
    # warehouse_name = #get from form
    # product_name = #get from form
    # product_quantity = #get from form

    obj = InventoryWarehouse(warehouse_name=warehouse_name, product_name=product_name, product_quantity=product_quantity)
    db.session.add(obj)
    db.session.commit()
           
    return render_template("homepage.html")


@app.route("/check_inventory_warehouse", methods=["GET"])
def check_inventory_warehouse():
    """Allows user to search for inventory items"""
    
    #query the inventory table to get info to display
    #query the warehouse table to get info to display
           
    return render_template("homepage.html")




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)