import praw

client_ID_input = input('Client ID: ')
client_secret_input = input('Client Secret: ')
username_input = input('Username: ')
password_input = input('Password: ')
subreddit_input = input('Subreddit: ')

reddit = praw.Reddit(client_id=client_ID_input,
                     client_secret=client_secret_input,
                     username=username_input,
                     password=password_input,
                     user_agent='testscript v.1 by AzureIllusion512')

subreddit = reddit.subreddit(subreddit_input)

for comment in subreddit.stream.comments():
    print(comment.body)
