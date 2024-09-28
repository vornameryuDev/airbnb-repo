from django.db import models

from common.models import CommomModel



class Like(CommomModel):
	user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='likes')
	tweet = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE, related_name='likes')

	def __str__(self):
		return self.user.username