

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
    
    
    def articles(self):
        return self._articles
    

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        magazines = self.magazines()
        if not magazines:
            return None
        return list(set(mag.category for mag in magazines))
    

    def magazines(self):
        return list(set(article.magazine for article in self._articles))
    
    
    
from article import Article
from magazine import Magazine


    




    
     

        
        