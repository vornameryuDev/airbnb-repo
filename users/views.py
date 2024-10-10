from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from tweets.serializers import TweetSerializer
from users import serializers
from users.models import User
from users.serializers import AllUserSerializer, UserCreateSerializer, UserSerializer
from django.contrib.auth import authenticate, login, logout



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
	
	def post(self, request):
		serializer = UserCreateSerializer(data=request.data)
		if serializer.is_valid():
			new_user = serializer.save() #password: set_password
			return Response(
				data=UserSerializer(new_user).data,
				status=status.HTTP_201_CREATED
			)
		else:
			return Response(
				data=serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)


class UserDetail(APIView):

	permission_classes = [IsAuthenticated]

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
	

class ChangePassword(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request):
		return Response(
			{
				'ok':True
			}
		)
	
	def put(self, request):
		user = request.user
		old_password = request.data.get('old_password')
		new_password = request.data.get('new_password')

		if not old_password or not new_password:
			raise exceptions.ParseError('둘다 입력하세요')

		if user.check_password(old_password):
			user.set_password(new_password)
			user.save()
			return Response(
				data={'change-password': True},
				status=status.HTTP_200_OK
			)
		else:
			raise exceptions.ParseError('old_password가 다릅니다.')

class Login(APIView):

	def post(self, request):
		username = request.data.get('username')
		password = request.data.get('password')

		if not username or not password:
			raise exceptions.ParseError('id와 pw를 모두 입력하세요')
		
		user = authenticate(
			request=request,
			username=username,
			password=password
		)

		if user:
			login(request=request, user=user)
			return Response(
				data={'login':True},
				status=status.HTTP_200_OK
			)
		else:
			raise exceptions.ParseError('입력한 id와 pw를 확인하세요')		


class Logout(APIView):

	permission_classes = [IsAuthenticated]
	
	def post(self, request):
		logout(request)
		return Response(
			data={'logout': True},
			status=status.HTTP_200_OK
		)