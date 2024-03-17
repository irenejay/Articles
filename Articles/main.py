from author import Author
from article import Article
from magazine import Magazine


try: 
  
  author1 = Author("Irene")
  print("Author name" , author1.name)



except ValueError as e:
    print("error author isntance " , e)


try: 
  
  magazine1 = Magazine("Tech Review", "Technology")
  magazine2 = Magazine("Science Today", "Science")
  print("Magazine name: " , magazine1.name)
  print("Magazine category: " , magazine1.category)
 

except ValueError as e:
    print("error author isntance " , e)


try: 
 
  author2 = Author("Mary")
  article1 = Article(author1, magazine1, "The future of AI")
  article2 = Article(author1, magazine1, "The Daily Tech")
  article3 = Article(author2,magazine2, "Germination Process")
  print("Atricle name: " , article1.title)
  print("Atricle author: " , article1.author.name)
  print("Atricle magazine: " , article1.magazine.name)
  

except ValueError as e:
    print("error author instance " , e)


try: 
  article4 = author1.add_article(magazine1, "AI Trends")
  article5 = author1.add_article(magazine2, "Science Breakthroughs")
  article6 = author2.add_article(magazine1, "ML applications")

  print("\n Author's articles ")
  for article in author1.articles():
    print("-" , article.title)

   
except ValueError as e:
    print("error author isntance " , e)



try: 
    top_magazine = Magazine.top_publisher()
    if top_magazine:
       print("\n Top Publisher: " , top_magazine.name)
    else: 
       print("\n Articles not sufficient,top publisher cannot be determined.")
except ValueError as e:
    print("error author isntance " , e)




