
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

from author import Author
from magazine import Magazine
