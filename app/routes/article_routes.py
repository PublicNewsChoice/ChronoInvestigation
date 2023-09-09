from flask import render_template, redirect, url_for, request, flash, Blueprint
from app import db
from app.models import Article
from app.forms import ArticleForm

article_routes = Blueprint('article_routes', __name__)


@article_routes.route('/articles', methods=['GET'])
def list_articles():
    articles = Article.query.all()
    return render_template('article/list.html', articles=articles, title='Articles')


@article_routes.route('/articles/new', methods=['GET', 'POST'])
def create_article():
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(
            title=form.title.data,
            url=form.url.data,
            source=form.source.data,
            publication_date=form.publication_date.data,
            summary=form.summary.data
        )
        db.session.add(article)
        db.session.commit()
        flash('Article created successfully.', 'success')
        return redirect(url_for('article_routes.list_articles'))
    return render_template('article/create.html', form=form, title='Create Article')


@article_routes.route('/articles/<int:id>', methods=['GET'])
def view_article(id):
    article = Article.query.get_or_404(id)
    return render_template('article/detail.html', article=article, title='Article Details')


@article_routes.route('/articles/<int:id>/edit', methods=['GET', 'POST'])
def edit_article(id):
    article = Article.query.get_or_404(id)
    form = ArticleForm(obj=article)

    if form.validate_on_submit():
        article.title = form.title.data
        article.url = form.url.data
        article.source = form.source.data
        article.publication_date = form.publication_date.data
        article.summary = form.summary.data

        db.session.commit()
        flash('Article updated successfully.', 'success')
        return redirect(url_for('article_routes.view_article', id=article.id))

    return render_template('article/edit.html', form=form, title='Edit Article', article=article)


@article_routes.route('/articles/<int:id>/delete', methods=['POST'])
def delete_article(id):
    article = Article.query.get_or_404(id)

    db.session.delete(article)
    db.session.commit()
    flash('Article deleted successfully.', 'success')

    return redirect(url_for('article_routes.list_articles'))
