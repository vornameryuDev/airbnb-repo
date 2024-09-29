from django.db import models

from common.models import CommomModel



class Tweet(CommomModel):
	payload = models.TextField(max_length=180, null=True)
	user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='tweets')
	
	def __str__(self):
		return self.payload
	
	def like_count(tweet):
		return tweet.likes.count()
