import pandas as pd # library used for working with dataset (analyzing, cleaning , exploring and manipulating data)
import requests   # library that handles the HTTP calls
from bs4 import BeautifulSoup # library that is use for parsing HTML and XML documents
from sqlalchemy import create_engine


# A simple web scrapping application to pull data from a web page

# Database credentials ( Note : never display your db opening like this in your main code)
db_user_name = 'postgres'
db_password = 'root'
host = 'localhost'
port = 5432
db_name = 'universityDB'
