import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        results = response.json().get("data")
        subscribers = results.get("subscribers")
        print(subscribers)  # Print the subscriber count
        return subscribers

    except requests.exceptions.RequestException as e:
        print("Error fetching subreddit data:", e)
        return 0
