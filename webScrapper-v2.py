 # This version 2 of the web scrapper

# Database credentials
# Note : Never open your db credential like this 
db_user_name = 'postgres'
db_password = 'root'
host = 'localhost'
port = 5432
db_name = 'universityDB'


# Data Extraction layer
def extract_data():
    data = pd.DataFrame()
    url = 'https://en.wikipedia.org/wiki/List_of_universities_in_England'
    scrapped_data = requests.get(url)
    scrapped_data = scrapped_data.content
    soup = bs(scrapped_data, 'lxml')
    html_data = str(soup.find_all('table')[0])
    df = pd.read_html(html_data)[0]
    df.to_csv('Data-file/wikipedia_data_v2_england.csv', index= False)
    print('Data Successfully written a csv file')