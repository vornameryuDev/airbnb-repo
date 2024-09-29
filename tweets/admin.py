from django.contrib import admin

from tweets.models import Tweet



@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

	list_display = (
		'payload',
		'user',
		'like_count',
		'created_at',
		'updated_at',
	)

