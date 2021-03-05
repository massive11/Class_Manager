from flask import Blueprint
from . import admin

admin = Blueprint('admin', __name__, template_folder='templates')
