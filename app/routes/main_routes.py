from flask import render_template, Blueprint, request, redirect, url_for, flash
from app.models import Organization, Person, Event, Action, Timeline, Article  # Import Article model
from app.database import db
from app.forms import ArticleForm  # Import Article form

main = Blueprint('main', __name__)

# Existing routes...

@main.route('/')
@main.route('/home')
def home():
    articles = Article.query.all()  # Query all articles from the database
    return render_template('index.html', title='Home', articles=articles)  # Pass the articles to the template

@main.route('/about')
def about():
    return render_template('about.html', title='About')

# ... (keep the existing routes for organizations, people, events, etc. as they are) ...

@main.route('/articles')  # New route for listing articles
def articles():
    articles = Article.query.all()
    return render_template('article/list.html', title='Articles', articles=articles)

@main.route('/article/create', methods=['GET', 'POST'])  # New route for creating articles
def create_article():
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(
            title=form.title.data,
            url=form.url.data,  # Added url field
            source=form.source.data,  # Added source field
            publication_date=form.publication_date.data,  # Added publication_date field
            summary=form.summary.data,  # Changed content to summary
        )
        db.session.add(article)
        db.session.commit()
        flash('Article created successfully!', 'success')
        return redirect(url_for('main.articles'))
    return render_template('article/create.html', title='Create Article', form=form)

@main.route('/article/<int:id>')  # New route for viewing article details
def article_detail(id):
    article = Article.query.get_or_404(id)
    return render_template('article/detail.html', title='Article Detail', article=article)

@main.route('/article/edit/<int:id>', methods=['GET', 'POST'])  # New route for editing articles
def edit_article(id):
    article = Article.query.get_or_404(id)
    form = ArticleForm(obj=article)
    if form.validate_on_submit():
        article.title = form.title.data
        article.url = form.url.data  # Added url field
        article.source = form.source.data  # Added source field
        article.publication_date = form.publication_date.data  # Added publication_date field
        article.summary = form.summary.data  # Changed content to summary
        db.session.commit()
        flash('Article updated successfully!', 'success')
        return redirect(url_for('main.article_detail', id=id))
    return render_template('article/edit.html', title='Edit Article', form=form, article=article)

@main.route('/article/delete/<int:id>', methods=['POST'])  # New route for deleting articles
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    flash('Article deleted successfully!', 'success')
    return redirect(url_for('main.articles'))

# ... (keep the remaining existing routes for timeline creator, linking, visualization, etc. as they are) ...
