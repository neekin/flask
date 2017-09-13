from flask import render_template
from . import error

@error.app_errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'),404
    
@error.app_errorhandler(500)
def internal_server_errors(e):
    return render_template('500.html'),500