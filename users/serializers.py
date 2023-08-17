from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'is_superuser',
            'email',
            'username',
            'password',
            'app_id',
            'dev_id',
            'cert_id',
            'ebay_token'
        ]