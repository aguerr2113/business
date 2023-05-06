import os
from flask import Flask, render_template, request, url_for, send_from_directory
from flask_mail import Mail, Message

app = Flask(__name__)

# Set the directory where the static files are located
app.static_folder = 'static'

# Define a route to serve the static files
@app.route('/static/<path:path>')
def serve_static(path):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, app.static_folder), path)

# Define the route for the homepage
@app.route('/')
def index():
    print(os.path.abspath(app.static_folder))

    return render_template('index.html')
