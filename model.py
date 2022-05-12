from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# class User(db.Model):
#     """A user."""

#     __tablename__ = 'users'

#     id = db.Column(db.Integer,
#                         autoincrement=True,
#                         primary_key=True)
#     name = db.Column(db.String, unique=False)
#     email = db.Column(db.String, unique=True)
#     password = db.Column(db.String)


#     def __repr__(self):
#         return f'<User user_id={self.id} email={self.email}>'
    
    
class Inventory(db.Model):
    """Table to keep track of inventory items"""

    __tablename__ = 'inventory'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    product_code = db.Column(db.Integer, unique=True)
    name = db.Column(db.String, unique=False)
    description = db.Column(db.String, unique=False)
    quantity = db.Column(db.Integer)
    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouse.id"))

    warehouse = db.relationship("Warehouse", backref="inventory")

    def __repr__(self):
        return f'<Inventory product_code={self.product_code} name={self.name} quantity={self.quantity}>'


class Warehouse(db.Model):
    """Table to keep track of warehouses"""

    __tablename__ = 'warehouse'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String, unique=True)
    weather = db.Column(db.String, unique=False) #need to load the weather data here


    def __repr__(self):
        return f'<Warehouse id={self.id} name={self.name}>'


# class InventoryWarehouse(db.Model):
#     """Table to keep track of warehouses and their inventory"""

#     __tablename__ = 'inventory-warehouse'

#     id = db.Column(db.Integer,
#                         autoincrement=True,
#                         primary_key=True)
#     warehouse_name = db.Column(db.String, db.ForeignKey("warehouse.name"), nullable=False)
#     product_name = db.Column(db.String, db.ForeignKey("inventory.name"), nullable=False)

#     inventory = db.relationship("Inventory", backref="inventory-warehouse")
#     warehouse = db.relationship("Warehouse", backref="inventory-warehouse")

#     def __repr__(self):
#         return f'<InventoryWarehouse name={self.name} product_name={self.product_name}>'


# def example_data():
#     """Create some sample data."""

#     Category.query.delete()
#     Ride.query.delete()

#     adults = Category(name="Adults")
#     thrill = Category(name="Thrill")
#     kid = Category(name="Kid")

#     user = User(email="quorra@hotmail.com", password="1234")

#     hm = Ride(name="Haunted Mansion")
#     mb = Ride(name="Matterhorn Bobsleds")
#     mtp = Ride(name="Mad Tea Party")

#     db.session.add_all([adults, thrill, kid, hm, mb, mtp, user])
#     db.session.commit()

def connect_to_db(app, db_uri="postgresql://popkjngt:VvqKa5kCap5HUaVA0DapnqqOVf6RHSxV@heffalump.db.elephantsql.com/popkjngt", echo=False):
    """Connect the database to the Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = echo
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
