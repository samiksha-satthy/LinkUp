from .models import Post, Comment
from rest_framework import serializers
from account.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'body', 'likes_count', 'comments_count', 'created_at_formated', 'created_by', ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'created_at_formated', 'created_by', ]

class PostDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['id', 'body', 'likes_count', 'comments_count', 'created_at_formated', 'created_by', 'comments_count', 'comments']