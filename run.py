from flask import Flask
from app.routes import main  # Import the Blueprint object from your routes.py file
from config import SECRET_KEY
from flask_jwt_extended import JWTManager

app = Flask(__name__, template_folder="app/templates")
# Configure the app using the config.py file
jwt = JWTManager(app)

app.config.from_object('config')

# Register the main Blueprint for routes
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
