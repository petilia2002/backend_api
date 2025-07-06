from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "static")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
