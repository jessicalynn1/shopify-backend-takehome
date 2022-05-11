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



@app.route("/user_homepage")
def user_homepage():
    """Asks what you'd like to do."""

    return render_template("user_homepage.html")


@app.route("/create_inventory", methods=["POST"])
def create_inventory():
    """Allows user to create a new inventory item"""
    
    product_code = request.form.get("product-code")
    name = request.form.get("name")
    quantity = request.form.get("quantity")

    new_product = Inventory(product_code=product_code, name=name, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()
           
    return 


@app.route("/edit_inventory", methods=["POST"])
def edit_inventory():
    """Allows user to edit an existing inventory item"""
    
    #query the inventory table to get item
    #get new input/data that needs to be changed from form
    #send inventory item back to database with changes

    edited = Inventory(product_code=product_code, name=name, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()
           
    return 


@app.route("/delete_inventory", methods=["POST"])
def delete_inventory():
    """Allows user to delete an existing inventory item"""
    
    #query the inventory table to get item
    #delete the item
    #send inventory item back to database deleted

           
    return 


@app.route("/create_warehouse", methods=["POST"])
def create_warehouse():
    """Allows user to create a new warehouse location"""
    
    location = request.form.get("location")
    db_location = Warehouse.query.filter_by(name=location).first()

    if not db_location:
        warehouse_location = Warehouse(name=location)
        db.session.add(warehouse_location)
        db.session.commit()

        return 


@app.route("/inventory_warehouse", methods=["POST"])
def inventory_warehouse():
    """Allows user to assign inventory to warehouse location"""
    
    # warehouse_name = #get from form
    # product_name = #get from form
    # product_quantity = #get from form

    obj = InventoryWarehouse(warehouse_name=warehouse_name, product_name=product_name, product_quantity=product_quantity)
    db.session.add(obj)
    db.session.commit()
           
    return 

@app.route("/check_inventory", methods=["GET"])
def check_inventory():
    """Allows user to search for inventory items"""
    
    #query the inventorywarehouse table to get info to display
           
    return 




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)