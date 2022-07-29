from flask import Flask
import re

DATABASE = "python_project"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
UPLOAD_FOLDER = 'app/static/img/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.secret_key = "123"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER