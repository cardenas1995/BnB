from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app
app = Flask(__name__)

# Configure your database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'  # Update with your credentials

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Import routes after the app is initialized to avoid circular imports
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
