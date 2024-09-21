from rest_framework import serializers

from apps.users.models import User


class UserAuthSerializer(serializers.ModelSerializer):
    avatar = serializers.CharField(source='avatar.url')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'avatar']
