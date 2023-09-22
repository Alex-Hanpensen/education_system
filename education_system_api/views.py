from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Lesson, User
from .serializers import UserSerializer, LessonSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class LessonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lesson.objects.filter()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

# django debug toolbar