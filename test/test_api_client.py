# Put your unit tests here
import requests
import sys
sys.path.append("/path/to/directory/containing/modules")

class JSONPlaceholderAPIClient:
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com'

    def get_posts(self):
        """
        Retrieves all posts from the JSONPlaceholder API.
        Returns: List of post objects.
        """
        url = f"{self.base_url}/posts"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve posts. Status code: {response.status_code}")
            return []

    def get_users(self):
        """
        Retrieves all users from the JSONPlaceholder API.
        Returns: List of user objects.
        """
        url = f"{self.base_url}/users"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve users. Status code: {response.status_code}")
            return []

    def get_json_schema(self, post_id):
        """
        used for  extract JSON schema for table structure
        """
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrive output for postid {post_id}. Status code: {response.status_code}")
            return []

if __name__ == "__main__":
    client = JSONPlaceholderAPIClient()
    posts = client.get_posts()
    users = client.get_users()
    
 #UATCASE Executing the api_client.py, will output 5 records for posts & users.
    print(posts[:5])  # Print first 5 posts as an example
    print(users[:5])  # Print first 5 users as an example