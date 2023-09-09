from flask import render_template, redirect, url_for, request, Blueprint
from app import db
from app.models import Action, Article
from app.forms import ActionForm, ArticleForm

action_routes = Blueprint('action_routes', __name__)

@action_routes.route('/actions', methods=['GET'])
def list_actions():
    actions = Action.query.all()
    return render_template('action/list.html', actions=actions)

@action_routes.route('/action/<int:id>', methods=['GET'])
def action_detail(id):
    action = Action.query.get_or_404(id)
    return render_template('action/detail.html', action=action)

@action_routes.route('/action/create', methods=['GET', 'POST'])
def create_action():
    form = ActionForm()
    if form.validate_on_submit():
        action = Action(name=form.name.data, description=form.description.data, date=form.date.data)
        article_ids = form.article_ids.data
        if article_ids:
            articles = Article.query.filter(Article.id.in_(article_ids)).all()
            action.articles.extend(articles)
        db.session.add(action)
        db.session.commit()
        return redirect(url_for('action_routes.list_actions'))
    return render_template('action/create.html', form=form)

@action_routes.route('/action/edit/<int:id>', methods=['GET', 'POST'])
def edit_action(id):
    action = Action.query.get_or_404(id)
    form = ActionForm(obj=action)
    if form.validate_on_submit():
        action.name = form.name.data
        action.description = form.description.data
        action.date = form.date.data
        # Updating the articles associated with the action
        article_ids = form.article_ids.data
        if article_ids:
            action.articles = Article.query.filter(Article.id.in_(article_ids)).all()
        db.session.commit()
        return redirect(url_for('action_routes.action_detail', id=id))
    return render_template('action/edit.html', form=form, action=action)

@action_routes.route('/action/delete/<int:id>', methods=['POST'])
def delete_action(id):
    action = Action.query.get_or_404(id)
    db.session.delete(action)
    db.session.commit()
    return redirect(url_for('action_routes.list_actions'))
