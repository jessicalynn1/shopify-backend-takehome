from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db, Inventory, Warehouse

from jinja2 import StrictUndefined
import webbrowser
import requests
import json 
from pprint import pprint

app = Flask(__name__, static_url_path='/static') 
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route("/")
def homepage():
    """Asks what you'd like to do."""

    return render_template("homepage.html")


@app.route("/create_inventory", methods=["POST"])
def create_inventory():
    """Allows user to create a new inventory item"""
    
    product_code = request.form.get("product-code")
    name = request.form.get("name")
    description = request.form.get("description")
    quantity = request.form.get("quantity")
    warehouse_name = request.form.get("warehouse")
    warehouse_id = Warehouse.query.filter_by(name=warehouse_name).first()
    #create drop down menu to pick warehouse

    new_product = Inventory(product_code=product_code, name=name, description=description, quantity=quantity, warehouse_id=warehouse_id.id)
    db.session.add(new_product)
    db.session.commit()
           
    return render_template("create_inventory.html")


@app.route("/edit_inventory", methods=["POST"])
def edit_inventory():
    """Allows user to edit an existing inventory item"""
    
    edit_name = request.form.get("name")
    edit_desc = request.form.get("description") 
    edit_quantity = request.form.get("quantity")
    edit_warehouse = request.form.get("warehouse")
    product_code = Inventory.query.filter_by("").first()
    all_inventory = Inventory.query.all()
    print(all_inventory)

    edited = Inventory(product_code=product_code, name=edit_name, description=edit_desc, quantity=edit_quantity, warehouse_id=edit_warehouse)
    db.session.add(edited)
    db.session.commit()
           
    return render_template("edit_inventory.html", all_inventory=all_inventory)


@app.route("/delete_inventory", methods=["POST"])
def delete_inventory():
    """Allows user to delete an existing inventory item"""
    
    deleted = request.form.get("deleted") 
    item = Inventory.query.filter_by(name=deleted).first()
    db.session.delete(item)
    db.session.commit()
           
    return render_template("delete_inventory.html")


@app.route("/create_warehouse", methods=["POST"])
def create_warehouse():
    """Allows user to create a new warehouse location"""
    
    location = request.form.get("location")
    db_location = Warehouse.query.filter_by(name=location).first()
    #need to add weather here if i use that

    if not db_location:
        warehouse_location = Warehouse(name=location) #need to add weather here
        db.session.add(warehouse_location)
        db.session.commit()
    else:
        flash ("This warehouse location already exists.")

        return render_template("create_warehouse.html")


@app.route("/inventory_warehouse", methods=["POST"])
def inventory_warehouse():
    """Allows user to assign inventory to warehouse location"""
    
    warehouse_id = request.form.get("warehouse")
    product_code = request.form.get("product-code")
    product_name = request.form.get("product-name")
    product_desc = request.form.get("product-desc")
    quantity = request.form.get("quantity")

    obj = Inventory(product_code=product_code, name=product_name, description=product_desc, quantity=quantity, warehouse_id=warehouse_id)
    db.session.add(obj)
    db.session.commit()
           
    return render_template("inventory_warehouse.html")


@app.route("/view", methods=["GET"])
def view():
    """Allows user to search for inventory items"""
    
    inventory_table = Inventory.query.all()
    warehouse_table = Warehouse.query.all()

           
    return render_template("view_inventory.html", inventory_table=inventory_table, warehouse_table=warehouse_table)




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)