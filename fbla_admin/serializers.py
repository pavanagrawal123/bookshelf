from . import models

from rest_framework import serializers


class studentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.student
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'grade_level', 
        )


class bookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.book
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'author', 
            'genre', 
        )


class ebookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ebook
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


