"""Entry point for Flask Image Filters webapp."""

from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask import url_for
from image_filters import apply_filters

app = Flask(__name__)


@app.route('/')
def index_page():
    """Index page handler."""
    return render_template('index_page.html')


@app.route('/process', methods=['POST'])
def process_image():
    """Process image handler."""
    return 200  # TODO: implement process_image handler


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # set debug to False when in production
