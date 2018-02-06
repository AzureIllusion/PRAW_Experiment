import praw
from pymongo import MongoClient

client = MongoClient()
db = client.redditbotdb
submissions = db.submissions
comments = db.comments

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

for submission in subreddit.hot(limit=5):
    if not submission.stickied:
        # print(dir(submission))
        print('Title: {} \n'
              'Author: {} \n'
              'Created UTC: {} \n'
              'Fullame: {} \n'
              'Subreddit: {}'.format(submission.title,
                                     submission.author,
                                     submission.created_utc,
                                     submission.fullname,
                                     submission.subreddit))

        sub = {"title": submission.title,
               'author': str(submission.author),
               'time': submission.created_utc,
               'fullname': submission.fullname,
               'subreddit': str(submission.subreddit)
               }
        submissions.insert_one(sub)

        submission.comments.replace_more()
        for comment in submission.comments.list():
            print(16 * '-')
            # print(dir(comment))
            print('Parent ID: {} \n'
                  'Author: {} \n'
                  'Created UTC: {} \n'
                  'Fullname: {} \n'
                  'Subreddit: {}'.format(comment.parent_id,
                                         comment.author,
                                         comment.created_utc,
                                         comment.fullname,
                                         comment.subreddit))

            com = {'parent_id': comment.parent_id,
                   'author': str(comment.author),
                   'time': comment.created_utc,
                   'fullname': comment.fullname,
                   'subreddit': str(comment.subreddit)
                   }
            comments.insert(com)

    print(48 * '-')
