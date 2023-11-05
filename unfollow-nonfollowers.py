from instagrapi import Client
import time

username = "your_username"
password = "your_password"

client = Client()
client.login(username, password)
print(f"Logged in as {username}.")

# Get your followers
followers = client.user_followers(client.user_id)
print(f"{username} has {len(followers)} followers.")

# Get your followings
followings = client.user_following(client.user_id)
print(f"{username} is following {len(followings)} users.")

# Get your nonfollowers
nonfollowers = list(set(followings) - set(followers))
print(f"Which means that {len(nonfollowers)} users don't follow {username} back.")

# Unfollow your nonfollowers
for nonfollower in nonfollowers:
    client.user_unfollow(nonfollower)
    print(f"Unfollowed {nonfollower}.")
    time.sleep(60)


