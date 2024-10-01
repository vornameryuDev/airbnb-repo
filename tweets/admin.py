from typing import Any
from django.contrib import admin

from tweets.models import Tweet



class ElonMuskFilter(admin.SimpleListFilter):
	title = "Contain or Not Contain 'ElonMusk'"
	parameter_name = 'elonmusk'

	def lookups(self, request, model_admin):
		return [
			("contain", "Contain"),	
			("not_contain", "Not Contain"),
		]
	
	def queryset(self, request, queryset):
		word = self.value()
		if word=="contain":
			return queryset.filter(payload__contains='elonmusk')
		else:
			queryset
	

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

	list_display = (
		'payload',
		'user',
		'like_count',
		'created_at',
		'updated_at',
	)

	list_filter = ('created_at', ElonMuskFilter, )

	search_fields = ('payload', 'username__user',)



