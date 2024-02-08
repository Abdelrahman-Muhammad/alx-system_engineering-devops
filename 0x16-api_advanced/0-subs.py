import requests

def number_of_subscribers(subreddit):
    try:
        user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        response = requests.get(url, headers=user_agent)

        if response.status_code == 200:
            try:
                results = response.json()
                return results.get('data').get('subscribers')
            except json.JSONDecodeError as e:
                print("Invalid JSON response:", e)
        else:
            print("API request failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Network error:", e)

    return 0
