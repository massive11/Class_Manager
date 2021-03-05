from flask import Blueprint
from . import view

main = Blueprint('main', __name__, template_folder='templates')
