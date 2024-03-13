class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def add_article(self, article):
        if not isinstance(article, Article):
            raise ValueError("Article must be of type Article")
        self._articles.append(article)

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))


    

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

    def add_article(self, article):
        if not isinstance(article, Article):
            raise ValueError("Article must be of type Article")
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    @classmethod
    def top_publisher(cls):
        if not cls._magazines:
            return None
        return max(cls._magazines, key=lambda mag: len(mag.articles))





class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise ValueError("Title must be of type str")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        self._author = author
        self._magazine = magazine
        self._title = title
        author.add_article(self) 
        magazine.add_article(self) 

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        self._magazine = magazine

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

        
        