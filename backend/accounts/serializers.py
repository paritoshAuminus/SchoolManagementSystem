from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user.username, user.email, user.first_name, user.last_name
        

