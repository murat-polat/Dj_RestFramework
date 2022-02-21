from dataclasses import fields
from rest_framework import serializers
from newusers.models import NewUser

class CreateUser(serializers.ModelSerializer):
    class meta:
        model = NewUser
        fields = '__all__'