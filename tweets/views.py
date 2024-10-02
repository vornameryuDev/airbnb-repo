from django.http import HttpResponse
from django.shortcuts import render

from tweets.models import Tweet





def all_tweets(request):

	tweets = Tweet.objects.all()

	return render(
		request=request,
		template_name='all_tweets.html',
		context={
			'tweets': tweets
		}
	)