from rest_framework import serializers
from ..models import Problem, Attempt


class ProblemSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title')
    difficulty_title = serializers.CharField(source='get_difficulty_display')
    is_solved = serializers.SerializerMethodField()
    is_attempted = serializers.SerializerMethodField()

    def get_is_solved(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Attempt.objects.filter(user=user, problem=obj, verdict=Attempt.Verdict.ACCEPTED).exists()
        else:
            return False

    def get_is_attempted(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Attempt.objects.filter(user=user, problem=obj).exists()
        else:
            return False

    class Meta:
        model = Problem
        fields = ['id', 'title', 'category_title', 'difficulty', 'difficulty_title',
                  'is_solved', 'is_attempted']
