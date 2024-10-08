from rest_framework import serializers
from users.models import User




class UserCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = (
			"username",
			"password"			
		)


class AllUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			"pk",
			"username",
			"email"
		)
		

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"