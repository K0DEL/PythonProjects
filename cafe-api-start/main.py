from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name)
                for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=['GET', 'POST'])
def random():
    cafes = db.session.query(Cafe).all()
    random_cafe = choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


# HTTP GET - Read Record
@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    all_cafes = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=all_cafes)


@app.route("/search")
def search():
    loc = request.args.get("loc")
    searched_cafes = db.session.query(Cafe).filter_by(location=loc).all()
    if searched_cafes:
        all_cafes = [cafe.to_dict() for cafe in searched_cafes]
        return jsonify(cafes=all_cafes)
    return jsonify(
        error={"Not Found": "Sorry, we don't have a cafe at that location"}
    )


# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record


@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_record(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        price = request.args.get("price")
        cafe.cofee_price = price
        db.session.commit()
        return jsonify(response={"success": "Cafe price updated."}), 200
    return jsonify(response={"error: No such record found."}), 404

# HTTP DELETE - Delete Record


@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    cafe_to_deleted = Cafe.query.get(cafe_id)
    if cafe_to_deleted:
        if api_key == "SuperSecretKey":
            db.session.delete(cafe_to_deleted)
            db.session.commit()
            return jsonify(response={"success": "Record was deleted"}), 200
        return jsonify(response={"error": "Not Authorised"}), 403
    return jsonify(response={"error": "No such record found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
