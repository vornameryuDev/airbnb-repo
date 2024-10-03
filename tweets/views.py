from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view



from tweets.models import Tweet
from tweets.serializers import TweetSerializer




@api_view()
def all_tweets(request):

	tweets = Tweet.objects.all()
	serializer = TweetSerializer(tweets, many=True)

	return render(
		request=request,
		template_name='all_tweets.html',
		context={
			'ok':True,
			'tweets': serializer.data,
		}
	)