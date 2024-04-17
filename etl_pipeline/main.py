# This is the main script where you will orchestrate the ETL process, feel free to completely modify the files/structure as you see fit.
from api_client       import JSONPlaceholderAPIClient
from transform_data   import transform_data
from load_to_database import loadtodb

if __name__ == "__main__":
    print("ETL Job Started")

    # Initialize API client
    client = JSONPlaceholderAPIClient()

    # Extract phase
    # TODO: Implement data extraction logic
    posts = client.get_posts()
    users = client.get_users()

    # Transform phase
    # TODO: Implement data transformation logic
    transformed_data = transform_data(posts, users)

    # Load phase
    # TODO: Implement data loading logic
    loader = loadtodb('gb_data_practice.db')
    loader.connect()
    loader.create_tables()
    loader.insert_records(transformed_data)
    loader.close_connection()

    print("ETL Job Finished")

