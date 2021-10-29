from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username', 'full_name', 'email', 'picture'
        ]

    def get_picture(self, obj: User):
        data = obj.get_social_data()
        return data.get('picture')
