from rest_framework import serializers

from apps.users.models import User, Group


class UserAuthSerializer(serializers.ModelSerializer):
    avatar = serializers.CharField(source='avatar.url')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'avatar', 'role']


class StudentSerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()

    @staticmethod
    def get_result(obj):
        return 1

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'result']


class GroupSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'students']
