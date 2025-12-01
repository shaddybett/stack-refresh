from flask import request, jsonify
from config import app, db
from models import Contact


# ------------------- GET ALL CONTACTS --------------------
@app.route('/contacts', methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = [c.to_json() for c in contacts]
    return jsonify({"contacts": json_contacts, "message": "Success"}), 200


# ------------------- CREATE CONTACT ---------------------
@app.route("/create_contact", methods=["POST"])
def create_contact():
    data = request.get_json()

    # Validation
    if not data.get("firstName") or not data.get("lastName") or not data.get("email"):
        return jsonify({"message": "All fields are required"}), 400

    new_contact = Contact(
        first_name=data["firstName"],
        last_name=data["lastName"],
        email=data["email"]
    )

    db.session.add(new_contact)
    db.session.commit()

    return jsonify({"message": "Contact added successfully"}), 201


# ------------------- UPDATE CONTACT ---------------------
@app.route("/update_contact/<int:id>", methods=["PUT"])
def update_contact(id):
    data = request.get_json()
    contact = Contact.query.get(id)

    if not contact:
        return jsonify({"message": "Contact not found"}), 404

    # Update only provided fields
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "Contact updated successfully"}), 200


# ------------------- DELETE CONTACT ---------------------
@app.route("/delete_contact/<int:id>", methods=["DELETE"])
def delete_contact(id):
    contact = Contact.query.get(id)

    if not contact:
        return jsonify({"message": "Contact not found"}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "Contact deleted successfully"}), 200


# ------------------- RUN APP ----------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)