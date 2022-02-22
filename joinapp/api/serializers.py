from dataclasses import fields
from rest_framework import serializers
from newusers.models import NewUser

class CreateUser(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['name', 'username', 'email', 'password', 'terms_of_service']

        # def create(self, validated_data):
        #     #profile_data = validated_data.pop('profile')
        #     user = NewUser.objects.create(**validated_data)
        #     #Profile.objects.create(user=user, **profile_data)
        #     return user