from urllib import request
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from users.serializers import AllUserSerializer, UserSerializer


@api_view()
def all_users(request):
	all_users = User.objects.all()
	serializer = AllUserSerializer(all_users, many=True)
	return Response(
		{
			'ok':True,
			'all_users': serializer.data
		}
	)


@api_view()
def user(request, user_pk):
	try:
		user = User.objects.get(pk=user_pk)
		serializer = UserSerializer(user)
		return Response(
			{
				'ok': True,
				'user': serializer.data
			}
		)
	except User.DoesNotExist:
		return Response(
			{
				'ok': False
			}
		)


def user_tweets(request, user_pk):
	tweets = User.objects.get(pk=user_pk).tweets.all()
	return render(
		request=request,
		template_name="user_tweets.html",
		context={'user_tweets': tweets}
	)

