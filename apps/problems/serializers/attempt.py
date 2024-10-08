from rest_framework import serializers

from apps.problems.models import Attempt


class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = '__all__'
