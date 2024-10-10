from flask import request, jsonify
from app import app, db
from models import User, Property, Booking  # Import the models

@app.route('/')
def home():
    return "Welcome to the BnB API!"

# Route to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# Route to add a new property
@app.route('/properties', methods=['POST'])
def add_property():
    data = request.get_json()
    new_property = Property(name=data['name'], location=data['location'], price=data['price'])
    db.session.add(new_property)
    db.session.commit()
    return jsonify({"message": "Property added successfully"}), 201

# Route to book a property
@app.route('/book', methods=['POST'])
def book_property():
    data = request.get_json()
    new_booking = Booking(user_id=data['user_id'], property_id=data['property_id'], booking_date=data['booking_date'])
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({"message": "Property booked successfully"}), 201

# Route to view all bookings for a user
@app.route('/users/<int:user_id>/bookings', methods=['GET'])
def view_bookings(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    bookings = [{'property_id': booking.property_id, 'booking_date': booking.booking_date} for booking in user.bookings]
    return jsonify(bookings), 200
