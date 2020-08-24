# Search-Engine

This is a project that I did to get a basic understanding of using Flask, SQLAlchemy and BeautifulSoup.

This project aims at building a site that has same functionalities as a google search engine.

Used search() from python package 'google'. The following link tells more about it.
(https://www.geeksforgeeks.org/performing-google-search-using-python-code/)

SQLAlchemy is used to store the metadata in a table. 

Flask is used to connect the database and the website. 

BeautifulSoup is used to scrape metadata of the links. This meta-data is stored in the database using SQLAlchemy. Then, Flask is used to fetch data from the table and is displayed on the webpage using Jinja template.

It is not as efficient as a typical search engine because of the sleep() function used to avoid any potential ip blocking.

Steps To Run:

Assumptions: Flask, SQLAlchemy and other dependencies are installed.

1) Open Terminal
2) Type FLASK_RUN=app.py FLASK_DEBUG=true flask run
3) Open browser and enter the port you are using as url. Eg: in this code it is 'localhost:5000'

Note: The webpage layout needs to be improved.