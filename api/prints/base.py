from flask import Blueprint, redirect

from model.cce import CCE

bp = Blueprint('base', __name__, url_prefix='/')

APP_VERSION = 'v0.1'

@bp.route('/')
def query():
    return redirect('/apidocs')
