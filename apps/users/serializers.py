from rest_framework import serializers

from apps.users.models import User, Group


class UserAuthSerializer(serializers.ModelSerializer):
    avatar = serializers.CharField(source='avatar.url')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'avatar', 'role']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'avatar', 'role']
