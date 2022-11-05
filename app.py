"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, render_template, flash, jsonify
#from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake, DEFAULT_IMAGE

app = Flask(__name__)
app.config['SECRET_KEY'] = '6uar1n0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

with app.app_context():
    db.create_all()


@app.route('/')
def homepage_route():
    """default homepage route"""

    return render_template("index.html")

@app.route('/test')
def homepage_route_test():
    """default homepage route"""

    return render_template("test.html")

@app.route('/api/cupcakes')
def get_all_cupcakes():
    """Get data about all cupcakes and return in JSON."""

    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """Get data about a single cupcakes and return in JSON."""

    cupcake = Cupcake.query.get_or_404(cupcake_id).serialize()
    return jsonify(cupcake=cupcake)


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Create a cupcake with flavor, size, rating and image data from the body of the request."""
    
    image_url = request.json["image"] if request.json["image"] else DEFAULT_IMAGE
    new_cupcake = Cupcake(
        flavor=request.json["flavor"],
        rating=request.json["rating"],
        size=request.json["size"],
        image=image_url
    )
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update a single cupcake's information"""

    update_cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    update_cupcake.flavor = request.json["flavor"]
    update_cupcake.rating = request.json["rating"]
    update_cupcake.size = request.json["size"]
    update_cupcake.image = request.json["image"]
    
    db.session.add(update_cupcake)
    db.session.commit()
    return jsonify(cupcake=update_cupcake.serialize())


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Delete a cupcake."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    message = "Cupcake has been deleted!"
    return jsonify(message=message)
