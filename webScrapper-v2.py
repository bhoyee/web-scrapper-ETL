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

    
# Data load transform and load layer
def transform_load_to_db():
    data = pd.read_csv('data/wikipedia_data_v2_england.csv') # Read csv file
    engine = create_engine(f'postgresql+psycopg2://{db_user_name}:{db_password}@{host}:{port}/{db_name}')
    data.to_sql('university_england_data_v2', con= engine, if_exists='replace', index= False)
    print('Data successfully written to PostgreSQL database')


def main():
    extract_data()
    transform_load_to_db()

main()


# this is just a simple script