from rest_framework import serializers
from app.models import *

class CreatedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'email', 'username', 'avatar')
        read_only_fields = ('first_name', 'last_name',
                            'email', 'username', 'avatar')


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('id', 'fullname', "email", "phone", "message",
                  "is_active", 'created_at', 'updated_at')


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ('id', 'name', 'is_active')


class BlogSerializer(serializers.ModelSerializer):
    created_by = CreatedBySerializer(many=False, read_only=True)
    category = BlogCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'name', 'description', 'category', 'image',
                  'alt', 'is_active', 'created_by', 'created_at', 'updated_at')
