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
    print 'Processing image'
    image_file = request.files['pic']
    image_file.seek(0)  # important!
    if image_file is None:
        return 400, 'Missing file'
    processed_file = apply_filters(image_file)
    return send_file(processed_file, cache_timeout=0, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # set debug to False when in production
