from flask import Flask

app = Flask(__name__)

from app import routes

# When microblog.py imports app (from app import app), it triggers the __init__.py file to execute.
# The __init__.py file creates the app instance and then imports routes.py, so all routes are registered before Flask starts running.