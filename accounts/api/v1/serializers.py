from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import Address

User = get_user_model()


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['city', 'street', 'postal_code']


class UserSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()
    addresses = AddressSerializer()

    class Meta:
        model = User
        fields = [
            'username', 'full_name', 'email', 'picture', 'phone_number', 'addresses'
        ]

    def get_picture(self, obj: User):
        data = obj.get_social_data()
        return data.get('picture')
