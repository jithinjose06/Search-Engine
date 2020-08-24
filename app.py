from googlesearch import search;
import requests
from bs4 import BeautifulSoup
from time import sleep
import random
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='postgresql://jithinjose@localhost:5432/search'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class SearchTable(db.Model):
	__tablename__='search_table'
	id=db.Column(db.Integer,primary_key=True)
	description = db.Column(db.String(),nullable=True)
	url = db.Column(db.String(),nullable=False)
	title = db.Column(db.String(),nullable=True)

	def __repr__(self):
		return f'<Todo {self.id}{self.description}>'

db.create_all()

def get_title(soup):
    """Scrape page title."""
    title = None
    if soup.find("title"):
        title = soup.find("title").string
    elif soup.find("meta", property="og:title"):
        title = soup.find("meta", property="og:title").get('content')
    elif soup.find("h1"):
        title = html.find("h1").string
    return title

def get_description(soup):
    """Scrape page description."""
    description = None
    if soup.find("meta", property="description"):
        description = soup.find("meta", property="description").get('content')
    elif soup.find("meta", property="og:description"):
        description = soup.find("meta", property="og:description").get('content')
    else:
        description = get_title(soup)
    return description

# render home page
@app.route('/')
def index():
	return render_template('index.html')
# render search page
@app.route('/search', methods = ['GET','POST'])
def second_page():
	db.session.query(SearchTable).delete()
	db.session.commit()
	query = request.form["query"]
	urlList = list(search(query,tld="com",num = 10,stop = 10)) # generate a list of links using search() function
	# iterate through list of links and scrape metadata
	for i in  urlList:
		sleep(random.randint(2,4))
		url = i
		page = requests.get(i)
		soup = BeautifulSoup(page.content,'html.parser')
		description = get_description(soup)
		title = get_title(soup)
		entry = SearchTable(description=description,url=i,title=title)
		db.session.add(entry)
		db.session.commit()
	return render_template('second.html',data = SearchTable.query.all())

