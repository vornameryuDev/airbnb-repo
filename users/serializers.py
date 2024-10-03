from rest_framework import serializers




class AllUserSerializer(serializers.Serializer):
	pk = serializers.IntegerField(
			read_only=True,
	)
	username = serializers.CharField(
		max_length=150,
	)


class UserSerializer(serializers.Serializer):
	
	pk = serializers.IntegerField(
			read_only=True,
	)
	username = serializers.CharField(
		max_length=150,
	)
	email = serializers.EmailField()
	is_active = serializers.BooleanField()