from flask import Blueprint, render_template

timeline_linking_bp = Blueprint('timeline_linking', __name__)

@timeline_linking_bp.route('/')
def index():
    return render_template('timeline_linking/index.html')
