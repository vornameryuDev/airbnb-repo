from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



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
	
	def post(self, request):		
		serializer = TweetSerializer(data=request.data)
		if serializer.is_valid():
			new_tweet = serializer.save(user=request.user) #user(FK)정보 전달
			return Response(
				data=TweetSerializer(new_tweet).data,
				status=status.HTTP_201_CREATED
			)
		else:
			return Response(
				data=serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)
	

class TweetDetail(APIView):

	def get_object(self, tweet_pk):		
		return Tweet.objects.get(pk=tweet_pk)


	def get(self, request, tweet_pk):
		tweet = self.get_object(tweet_pk=tweet_pk)
		serializer = TweetSerializer(tweet)
		return Response(
			data={'data': serializer.data},
			status=status.HTTP_200_OK
		)


	def put(self, request, tweet_pk):
		tweet = self.get_object(tweet_pk=tweet_pk)
		serializer = TweetSerializer(
			tweet,
			data=request.data,
			partial=True
		)
		if serializer.is_valid():
			updated_tweet = serializer.save(user=request.user)
			return Response(
				data=TweetSerializer(updated_tweet).data,
				status=status.HTTP_202_ACCEPTED
			)
		else:
			return Response(
				data=serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)


	def delete(self, request, tweet_pk):
		tweet = self.get_object(tweet_pk=tweet_pk)
		tweet.delete()
		return Response(
			data={'delete ok': True},
			status=status.HTTP_204_NO_CONTENT
		)


		
		

