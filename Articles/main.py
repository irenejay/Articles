from author import Author
from magazine import Magazine
from article import Article

author1 = Author("irene")
author2 = Author("sharon")


magazine1 = Magazine("Tech Magazine", "Technology")
magazine2 = Magazine("Science Weekly", "Science")

magazine1.add_article(author1, "The Future of AI")
magazine1.add_article(author2, "Latest Trends in Machine Learning")
magazine2.add_article(author1, "Discovering New Planets")


print("Contributors of Tech Magazine:")
for contributor in magazine1.contributors():
    print(contributor.name)


author2.add_article(magazine2, "The Impact of Quantum Computing")

# Getting articles of an author
print("Articles by Jane Smith:")
for article in author2.articles():
    print(article.title)

# Finding top publisher
top_publisher = Magazine.top_publisher()
if top_publisher:
    print(f"Top Publisher: {top_publisher.name}")
else:
    print("No magazines available.")


try:
    invalid_article = Article(author1, magazine2, 123)
except ValueError as e:
    print(f"Error: {e}")