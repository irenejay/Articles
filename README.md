# Articles


## Overview
 this system allows users to create authors, magazines, and articles, associate articles with authors and magazines, and perform various operations such as retrieving information about articles, authors, and magazines.
 
 
 ## Functionality
### Author Class
Initialization: Authors are initialized with a name.
 
 Properties:
name: Returns the author's name.

Methods:
 .articles(): Returns a list of all the articles the author has written.
 .magazines(): Returns a unique list of magazines for which the author has contributed to.
  .add_article(magazine, title): Creates and returns a new Article instance associated with the author and provided magazine.
### Magazine Class
Initialization: Magazines are initialized with a name and a category.
Properties:
name: Returns the magazine's name.
category: Returns the magazine's category.
Methods:
.articles(): Returns a list of all the articles the magazine has published.
.contributors(): Returns a unique list of authors who have written for this magazine.
.article_titles(): Returns a list of the titles of all articles written for that magazine.
.contributing_authors(): Returns a list of authors who have written more than 2 articles for the magazine.
.top_publisher(): Class method returning the Magazine instance with the most articles.
 ### Article Class
Initialization: Articles are initialized with an Author instance, a Magazine instance, and a title.
Properties:
title: Returns the article's title.
author: Returns the author object for that article.
magazine: Returns the magazine object for that article.
