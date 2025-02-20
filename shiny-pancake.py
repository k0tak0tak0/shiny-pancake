# I was trying to make a script to deduct blocked users from followers to get a real follower count
# But as far as I can tell the API already does that (even tho the app doesn't)
# The documentation does not explain what app.bsky.graph.get_followers does, so these are only assumptions.

from atproto import Client
from atproto.exceptions import AtProtocolError

# Replace with your Bluesky handle and app password
# Get yours at https://bsky.app/settings/app-passwords
BSKY_USERNAME = "YOUR-HANDLE.bsky.social"
BSKY_APP_PASSWORD = "YOUR-APP-PASSWORD"

# If you want to check the follower count of someone else, replace 'BSKY_USERNAME' with their handle 
BSKY_USERNAME_TO_CHECK = BSKY_USERNAME

def fetch_all_followers(client):
    """Fetch all followers using pagination and print debugging info.
       
       The API doesn't return all the followers at once, you have to keep calling
            the cursor until it doesn't return anyting anymore.
    """
    all_followers = set()
    cursor = None

    while True:
        try:
            params = {'actor': BSKY_USERNAME_TO_CHECK}
            if cursor:
                params['cursor'] = cursor

            response = client.app.bsky.graph.get_followers(params)
            followers = response.followers

            all_followers.update(follower.did for follower in followers)
            cursor = getattr(response, 'cursor', None)

            if not cursor:
                break  # No more pages

        except AtProtocolError as e:
            print(f"Error fetching followers: {e}")
            break

    return all_followers


def get_follower_count():
    client = Client()
    
    try:
        client.login(BSKY_USERNAME, BSKY_APP_PASSWORD)
    except AtProtocolError as e:
        print(f"Login failed: {e}")
        return
    
    print("\nFetching followers...")
    followers_dids = fetch_all_followers(client)
    print(f"\nTotal Followers Retrieved: {len(followers_dids)}")


if __name__ == "__main__":
    get_follower_count()
