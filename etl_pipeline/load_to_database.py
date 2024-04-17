import sqlite3
from transform_data import transform_data  
from api_client     import  JSONPlaceholderAPIClient

class loadtodb:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.inserted_rows = 0  # to check the count of rows inserted

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

     # script will create table if not exists.
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS GB_posts (
                id INTEGER PRIMARY KEY,
                userId INTEGER,
                title TEXT,
                body TEXT,
                status TEXT,
                username TEXT,
                email TEXT
            )
        ''')
        self.connection.commit()

    def insert_records(self, posts):
     for post in posts:
        user = post.get('user')  # Check if 'user' exists
        if user:
            username = user.get('username')
            email    = user.get('email')
        else:
            # If 'user' does not exist, set username and email to None
            username = None
            email    = None

        self.cursor.execute('''
            INSERT INTO GB_posts (id, userId, title, body, status, username, email)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (post['id'], post['userId'], post['title'], post['body'], post['status'], username, email))
        
        self.inserted_rows += 1
     self.connection.commit()

    def close_connection(self):
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    client = JSONPlaceholderAPIClient()

    posts = client.get_posts()
    users = client.get_users()
    transformed_data = transform_data(posts, users)

    loader = loadtodb('gb_data_practice.db')
    loader.connect()
    loader.create_tables()
    loader.insert_records(transformed_data)
    loader.close_connection()
