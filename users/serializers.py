from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer


class LoginSerializer(RestAuthLoginSerializer):
    username = None

class CustomRegisterSerializer(RegisterSerializer):
    username = None    
    country = serializers.CharField(max_length=30)
    state = serializers.CharField(max_length=30)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.country = self.data.get('country')
        user.state = self.data.get('state')
        user.save()
        return user

from users.models import CustomUser


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'pk',
            'email',
            'country',
            'state',
        )
        read_only_fields = ('pk', 'email', )


