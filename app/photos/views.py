from . import photos
from flask import render_template
@photos.route("/")
def index():
    return render_template('/photos/index.html')