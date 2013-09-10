import twitter
import time

api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')


user = '@UserName'
statuses = api.GetUserTimeline(screen_name=user, count=1)

initial_status = [s.text.replace('@', '') for s in statuses]

while True:
	statuses = api.GetUserTimeline(screen_name=user, count=1)
	current_status = [s.text.replace('@', '') for s in statuses]
	if initial_status != current_status:
		status = api.PostUpdate(current_status)
		print(status.text)

		initial_status = current_status
	else:
		print("Nothing has changed in 20 seconds.")
		print(current_status)
		time.sleep(20)


