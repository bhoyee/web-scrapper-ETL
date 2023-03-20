# - Build us a system to pull data to the database
# - Refreshed every hour


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


# Data Extraction layer
def extract_data():
    url = 'https://en.wikipedia.org/wiki/List_of_universities_in_Nigeria'
    scrapped_data = requests.get(url)
    scrapped_data = scrapped_data.content
    soup = BeautifulSoup(scrapped_data, 'lxml')
    print(type(soup))
    list_of_rows = []   #[['University of Ibadan', 'Oyo State', 'UI', 1986 ], ['Convenant', 'Ogun', 'CU', 1992 ]]
    for row in soup.findAll('tr'):
        list_of_cells = []     #['University of Ibadan', 'Oyo State', 'UI', 1986 ]
        for cell in row.findAll('td'):
            #text = cell.text.encode('utf-8')
            text = cell.text.replace('\n', '')
            #print(text)
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
        
    
    wiki_data = pd.DataFrame(list_of_rows[1:], columns= ['University Name', 'State', 'Abbrevation', 'Location', 'Status', 'Year found'])
    wiki_data.to_csv('Data-file/wikipedia_uni_nigeria_data.csv', index= False) #the data will be store inside the Data-file folder
    print('Data Successfully written a csv file')
    
# data loading layer
def load_data_to_db():
    data = pd.read_csv('data/wikipedia_uni_nigeria_data.csv') # Read csv file
    # Re-order columns
    data = data[['State', 'Abbrevation', 'Location', 'Status', 'Year found', 'University Name']]
    # conString = "postgres://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName"
    engine = create_engine(f'postgresql+psycopg2://{db_user_name}:{db_password}@{host}:{port}/{db_name}')
    data.to_sql('university_data', con= engine, if_exists='append', index= False)
    print('Data successfully written to PostgreSQL database')


extract_data()
load_data_to_db()
