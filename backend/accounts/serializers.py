from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Mets(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')


