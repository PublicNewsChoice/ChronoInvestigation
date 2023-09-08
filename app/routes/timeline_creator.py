from flask import Blueprint, render_template

timeline_creator_bp = Blueprint('timeline_creator', __name__)

@timeline_creator_bp.route('/')
def index():
    return render_template('timeline_creator/index.html')
