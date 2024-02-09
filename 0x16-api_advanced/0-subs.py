import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="YOUR_USER_AGENT",
    redirect_uri="YOUR_REDIRECT_URI",
)

def number_of_subscribers(subreddit):
    try:
        subreddit = reddit.subreddit(subreddit)
        return subreddit.subscriber_count

    except praw.exceptions.ClientException as e:
        print(f"Error fetching subreddit data: {e}")
        return 0
