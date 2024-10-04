from urllib import request
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from tweets.serializers import TweetSerializer
from users import serializers
from users.models import User
from users.serializers import AllUserSerializer, UserSerializer



class Users(APIView):
	def get(self, request):
		all_users = User.objects.all()
		serializer = AllUserSerializer(
			all_users,
			many=True,
			context={
				'request': request
			}
		)
		return Response(
			{
				'ok':True,
				'all_users': serializer.data
			}
		)


class UserDetail(APIView):
	def get_object(self, user_pk):
		try:
			user = User.objects.get(pk=user_pk)
			return user
		except User.DoesNotExist:
			return NotFound

	def get(self, request, user_pk):
		user = self.get_object(user_pk)
		serializer = UserSerializer(
			user,
			context={'request': request}
		)
		return Response(
			{
				'ok': True,
				'user': serializer.data
			}
		)


class UserTweets(APIView):
	def get_object(self, user_pk):
		try:
			user = User.objects.get(pk=user_pk)
			return user.tweets.all()
		except User.DoesNotExist:
			return NotFound
		
	def get(self, request, user_pk):
		tweets = self.get_object(user_pk)
		serializers = TweetSerializer(tweets, many=True)
		return Response(
			{
				'ok': True,
				'user_tweets': serializers.data
			}
		)