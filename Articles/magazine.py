# magazine.py
class Magazine:
    _magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be of type str")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        if not isinstance(category, str):
            raise ValueError("Category must be of type str")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._name = name
        self._category = category
        self._articles = []
        Magazine._magazines.append(self)

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def add_article(self, author, title):  
        new_article = Article(author, self, title)  
        self._articles.append(new_article)

    @property
    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def contributing_authors(self):
        authors = [author for author in self.contributors() if len(author.articles()) > 2]
        if not authors:
            return None
        return authors

    @classmethod
    def top_publisher(cls):
        if not cls._magazines:
            return None
        return max(cls._magazines, key=lambda mag: len(mag.articles))

    
    

from author import Author
from article import Article