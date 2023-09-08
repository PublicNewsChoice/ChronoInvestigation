from flask import Blueprint, render_template

interactive_visualization_bp = Blueprint('interactive_visualization', __name__)

@interactive_visualization_bp.route('/')
def index():
    return render_template('interactive_visualization/index.html')
