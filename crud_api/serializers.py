from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "upvotes", "link", "author")


class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "upvotes", "link")
