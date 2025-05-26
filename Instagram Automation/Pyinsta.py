from instagrapi import Client

cl = Client()

# Replace these with your real Instagram username/password
USERNAME = "rsquare_studios"
PASSWORD = "Letmein4@"

cl.login(USERNAME, PASSWORD)

profile = cl.account_info()
print("Logged in as:", profile.username)
