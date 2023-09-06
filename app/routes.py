from flask import Flask, Blueprint, request, make_response, render_template, jsonify, redirect
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import RATE_LIMIT_DEFAULT
from functools import wraps
 
# Create a Blueprint to define routes
main = Blueprint("main", __name__)

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app)

JWT_TOKEN = None

def authenticate_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check if the user is authenticated (you can implement your authentication logic here)
        print('jwt ',JWT_TOKEN)
        if JWT_TOKEN:
            return func(*args, **kwargs)
        else:
            return jsonify({"message": "Authentication failed"}), 401  # Unauthorized

    return wrapper


@main.route("/", methods=["GET"])
def index():
    global JWT_TOKEN
    JWT_TOKEN = None
    return render_template("login.html")

@main.route("/", methods=["POST"])
def post_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "purvipatil" and password == "purvi123":
        global JWT_TOKEN
        JWT_TOKEN = create_access_token(identity=username)
        return redirect('/upload')

    return redirect('/')

@main.route("/upload", methods=["GET"])
@authenticate_user
def upload_get():
    return render_template("index.html")

@main.route("/upload", methods=["POST"])
@authenticate_user
@limiter.limit(RATE_LIMIT_DEFAULT)
def upload():
    if "image" in request.files:
        image = request.files["image"]
        if image:
            image_name = image.filename
            return f"Uploaded Image Name: {image_name}"
    return "No image uploaded"


@main.route("/login", methods=["GET"])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == "purvipatil" and password == "purvi123":
        access_token = create_access_token(identity=username)
        response = make_response(jsonify({"message": "Login successful"}))
        response.headers['Authorization'] = f'Bearer {access_token}'
        response.set_cookie('access_token', access_token)        
        return response
    return "Not valid creds !!"

@main.route("/api/authenticate", methods=["POST"])
def authenticate():
    username = request.json.get("username")
    password = request.json.get("password")

    if username == "purvipatil" and password == "purvi123":
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200

    return jsonify({"message": "Authentication failed"}), 401
