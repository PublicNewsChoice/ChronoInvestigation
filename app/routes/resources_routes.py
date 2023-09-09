from flask import render_template, Blueprint

resource_routes = Blueprint('resources', __name__)

@resource_routes.route('/tutorials')
def tutorials():
    return render_template('resources/tutorials.html', title='Tutorials')

@resource_routes.route('/documentation')
def documentation():
    return render_template('resources/documentation.html', title='Documentation')

@resource_routes.route('/faq')
def faq():
    return render_template('resources/faq.html', title='FAQ')

@resource_routes.route('/contact')
def contact():
    return render_template('resources/contact.html', title='Contact Us')

@resource_routes.route('/feedback')
def feedback():
    return render_template('resources/feedback.html', title='Feedback')
