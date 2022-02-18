from dataclasses import fields
from rest_framework import serializers
from .models import NewUser

class CreateUser(serializers.ModelSerializer):
    class meta:
        model = NewUser
        fields = '__all__'