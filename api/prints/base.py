from flask import Blueprint, redirect, url_for

from model.cce import CCE

bp = Blueprint('base', __name__, url_prefix='/')

APP_VERSION = 'v0.0.1'

@bp.route('/')
def query():
    return redirect(url_for('flasgger.apidocs'))
