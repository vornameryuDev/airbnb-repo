from django.contrib import admin

from tweets.models import Tweet



@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

	list_display = (
		'payload',
		'user',
		'created_at',
		'updated_at',
	)

