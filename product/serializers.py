from rest_framework import serializers
from .models import Product, DeletedList, ProductDescription, ProductPhoto
from users.serializers import UserSerializer

class ProductDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDescription
        exclude = ['created_at', 'updated_at']

class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        exclude = ['created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):

    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        depth = 1

class DeletedListSerializer(serializers.ModelSerializer):

    created_by = UserSerializer(read_only=True)

    class Meta:
        model = DeletedList
        fields = "__all__"
        depth = 1
