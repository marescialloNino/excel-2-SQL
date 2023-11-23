import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

# Database connection parameters
db_username = 'your_user'
db_password = 'your_password'
db_host = 'localhost'
db_port = '5432'
db_name = 'your_db_name'

engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

def check_connection(engine):
    try:
        # Try to execute a simple query
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return True if result else False
    except OperationalError as e:
        print(f"Connection failed: {e}")
        return False

if check_connection(engine):
    print("Connection successful.")
else:
    print("Connection failed.")


def upload_file_to_db(file_path):
    
    if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        df = pd.read_excel(file_path)
        print(df)
    elif file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        print(df)

    # Extract the filename without extension and spaces to use as table name
    table_name = os.path.splitext(os.path.basename(file_path))[0].replace(' ', '_')

    # Upload the DataFrame to the database
    try:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Table {table_name} created successfully.")
    except Exception as e:
        print(f"Error while creating table {table_name}: {e}")


def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx') or filename.endswith('.xls') or filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            upload_file_to_db(file_path)
            print(f"Uploaded {filename} to table {filename.split('.')[0].replace(' ', '_')}")


folder_path = './excel-or-csv-files'

process_folder(folder_path)
