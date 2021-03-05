from flask import Blueprint
from . import teacher

teacher = Blueprint('teacher', __name__, template_folder='templates')
