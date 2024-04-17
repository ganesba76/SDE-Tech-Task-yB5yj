from api_client import JSONPlaceholderAPIClient

# Initialize API client
client = JSONPlaceholderAPIClient()

# Extract data from JSONPlaceholder API
posts = client.get_posts()
users = client.get_users()

# Function to transform the data
def transform_data(posts, users):
    user_dict = {user['id']: user for user in users}
    transformed_posts = []
    for post in posts:
        # Parsing embedded JSON structure
        post['jschema'] = client.get_json_schema(post['id'])

        # Add computed status column as per requirement
        post['status'] = 'lengthy' if len(post['body']) > 100 else 'concise'

        # Combine posts with user details
        user_id = post['userId']
        user_details = user_dict.get(user_id)
        if user_details:
           post['user'] = user_details

        transformed_posts.append(post)

    return transformed_posts

# Example usage:
transformed_data = transform_data(posts, users)
