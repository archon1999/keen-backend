from rest_framework import viewsets

from apps.problems.models import Problem
from apps.problems.serializers import ProblemListSerializer, ProblemDetailSerializer


class ProblemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Problem.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProblemListSerializer
        else:
            return ProblemDetailSerializer
