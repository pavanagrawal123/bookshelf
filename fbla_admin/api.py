from . import models
from . import serializers
from rest_framework import viewsets, permissions


class studentViewSet(viewsets.ModelViewSet):
    """ViewSet for the student class"""

    queryset = models.student.objects.all()
    serializer_class = serializers.studentSerializer
    permission_classes = [permissions.IsAuthenticated]


class bookViewSet(viewsets.ModelViewSet):
    """ViewSet for the book class"""

    queryset = models.book.objects.all()
    serializer_class = serializers.bookSerializer
    permission_classes = [permissions.IsAuthenticated]


class ebookViewSet(viewsets.ModelViewSet):
    """ViewSet for the ebook class"""

    queryset = models.ebook.objects.all()
    serializer_class = serializers.ebookSerializer
    permission_classes = [permissions.IsAuthenticated]


