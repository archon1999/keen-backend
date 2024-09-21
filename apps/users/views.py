from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.utils import translation
from rest_framework import viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.users.models import Group, User, RoleChoice
from apps.users.serializers import UserAuthSerializer, GroupSerializer, StudentSerializer
from core import settings


@api_view(["POST"])
@authentication_classes([SessionAuthentication,
                         TokenAuthentication])
def login(request: Request) -> Response:
    django_login(request, request.user)
    return Response(UserAuthSerializer(request.user).data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def logout(request: Request) -> Response:
    django_logout(request)
    return Response({})


@api_view(["GET"])
@authentication_classes([SessionAuthentication,
                         TokenAuthentication])
@permission_classes([IsAuthenticated])
def me(request: Request) -> Response:
    user = request.user
    return Response(UserAuthSerializer(user).data)


@api_view(["POST"])
def set_language(request: Request) -> Response:
    language = request.data['language']
    translation.activate(language)
    response = Response({})
    response.set_cookie(settings.KEENSettings.LANGUAGE_COOKIE_NAME,
                        language)
    return response


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['get']


class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(role=RoleChoice.STUDENT)
    serializer_class = StudentSerializer
    http_method_names = ['get']

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return super().get_queryset()

        group = Group.objects.filter(id=self.kwargs['group_id']).first()
        if group:
            return group.students.all()
        return self.queryset.none()
