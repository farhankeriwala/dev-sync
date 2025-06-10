"""
Serializers are used to convert complex data types into JSON and vice versa to be able to communicate between the API
and the client
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)  # Confirm password

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'bio',
            'github_link',
            'profile_image',
            'reputation_score'
        )
        read_only_fields = ('id', 'reputation_score')  # Prevent direct edits

#     {
# "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0OTY2ODcwMiwiaWF0IjoxNzQ5NTgyMzAyLCJqdGkiOiI1ZTg0ZDBiOWMzMjY0NTc3YTMzMmVlOTMxYjI2YWNjOSIsInVzZXJfaWQiOjJ9.wB466MOQMxkPQMw5B-Szv1vEw-eRQRFMpxApkAUMoEw",
# "access": ""
# }
