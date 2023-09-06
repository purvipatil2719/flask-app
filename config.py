import os

# Flask app secret key
SECRET_KEY = 'purvipatil2719'

# JWT configuration
JWT_SECRET_KEY = 'purvipatil2719'  # Replace with a strong, secret key
JWT_ACCESS_TOKEN_EXPIRES = False  # Access tokens won't expire for this example

# Rate limiting configuration
RATE_LIMIT_DEFAULT = "5 per minute"  # Default rate limit for API endpoints
RATE_LIMIT_HEADERS_ENABLED = True  # Include rate limit headers in responses

# File upload configuration
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # Folder to store uploaded files
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}  # Allowed file extensions for uploads
