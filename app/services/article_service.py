from app import db
from app.models import Article

def create_article(data):
    """
    Create a new article in the database
    :param data: Article data
    :return: Article object
    """
    article = Article(**data)
    db.session.add(article)
    db.session.commit()
    return article

def get_article_by_id(article_id):
    """
    Get an article by ID
    :param article_id: Article ID
    :return: Article object
    """
    return Article.query.get(article_id)

def get_all_articles():
    """
    Get all articles
    :return: List of Article objects
    """
    return Article.query.all()

def update_article(article_id, data):
    """
    Update an article by ID with new data
    :param article_id: Article ID
    :param data: New article data
    :return: Article object
    """
    article = get_article_by_id(article_id)
    for key, value in data.items():
        setattr(article, key, value)
    db.session.commit()
    return article

def delete_article(article_id):
    """
    Delete an article by ID
    :param article_id: Article ID
    :return: None
    """
    article = get_article_by_id(article_id)
    db.session.delete(article)
    db.session.commit()
