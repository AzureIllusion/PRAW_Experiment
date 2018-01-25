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

hot_posts = subreddit.hot(limit=5)

for submission in hot_posts:
    if not submission.stickied:
        print(submission)
        print('Title: {}, \n'
              'Original Poster: {} \n'
              'Vp votes: {}, Down votes: {} \n'
              'Viewed before: {}'.format(submission.title,
                                         submission.author,
                                         submission.ups,
                                         submission.downs,
                                         submission.visited))

        submission.comments.replace_more(limit=0)

        for comment in submission.comments:
            print(16 * '-')
            print('Parent ID: ', comment.parent())
            print('Comment ID: ', comment.id)
            print(comment.body)

    print(48 * '-')
