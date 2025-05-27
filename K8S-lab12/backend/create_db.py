import psycopg2
import os

def create_table():
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'postgres'),
        database=os.getenv('POSTGRES_DB', 'winecollection'),
        user=os.getenv('POSTGRES_USER', 'postgres'),
        password=os.getenv('POSTGRES_PASSWORD', 'yourpassword')
    )
    
    cursor = conn.cursor()
    
    # SQL to create table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS wines (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        year INT NOT NULL,
        type VARCHAR(255) NOT NULL
    );
    '''
    
    cursor.execute(create_table_query)
    conn.commit()
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_table()
