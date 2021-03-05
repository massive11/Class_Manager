from flask import Blueprint
from . import student

student = Blueprint('student', __name__, template_folder='templates')
