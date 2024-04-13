from flask import Flask, request
import json
from config import db

app = Flask(__name__) # is the server (root)

@app.get("/")# this is the API
def home(): # this is the API
    return "hello from flask" # this is the API

@app.get("/test")
def test():
    return "this is a test page"

@app.get("/about")
def test_about():
    me = {"name": "Jesse"}
    return json.dumps(me)

@app.get("/api/versions")
def versions():
    versions = {"version":"dog", "name": "mesha", "description": "the real newest version"}
    return json.dumps(versions)

@app.get("/admin")
def admin():
    return "hello im the admin"

@app.get("/api/products")
def get_products():
    products = []
    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.post("/api/products")
def save_products():
    prod = request.get_json()
    print (prod)
    #mock save
    #products.append(prod)
    db.products.insert_one(prod)
    return json.dumps(fix_id(prod))

@app.put("/api/products/<int:index>")# using put it replaces everything
def update_products(index):
    updated_product = request.get_json()
    if 0 <= index < len(products):
        products[0] = updated_product
        return json.dumps(updated_product)
    else:
        return "That index does not exist"

# use the same logic but remenber that you need to use list.pop
#create the logic for the delete API
@app.delete("/api/products/<int:index>")
def delete_products(index):
    deleted_product = request.get_json()
    if 0 <= index < len(products):
        deleted_product = products.pop(index)
        return json.dumps(deleted_product)
    else:
        return "That index does not exist"

@app.patch("/api/products/<int:index>")
def patch_products(index):
    updated_field = request.get_json()
    if 0 <= index < len(products):
        products(index).update(updated_field)
        return json.dumps(updated_field)
    else:
        return "That index does not exist"

@app.get("/api/footer")
def get_footer():
    return "hello im the footer"


app.run(debug=True)

