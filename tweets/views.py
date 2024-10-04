from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView



from tweets.models import Tweet
from tweets.serializers import TweetSerializer




class Tweets(APIView):

	def get(self, request):
		tweets = Tweet.objects.all()
		serializer = TweetSerializer(tweets, many=True)
		return Response(
			{
				'ok':True,
				'tweets': serializer.data
			}
		)
