import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API for the number of subscribers of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid or an error occurs.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'YourCustomUserAgent/1.0'}  # Replace with your custom User-Agent
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)  # Prevent redirects
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()
        return data.get('data', {}).get('subscribers')  # Handle potential missing keys

    except requests.exceptions.RequestException as e:
        print(f"Error fetching subreddit data: {e}")
        return 0
