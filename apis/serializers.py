from rest_framework import serializers
from projects import models

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'title',
            'url',
            'description',
            'photo',
            'author',
            'date_posted'

        )
        model=models.Post


     