from rest_framework import viewsets

from apps.problems.models import Problem
from apps.problems.serializers import ProblemSerializer


class ProblemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
