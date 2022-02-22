from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from newusers.models import NewUser
from .serializers import CreateUser 

@api_view(['GET', 'POST'])
def Register(request):
    new_user= NewUser.objects.all()
    serializer= CreateUser(new_user, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def AllUsers(request):
    new_user= NewUser.objects.all()
    serializer= CreateUser(new_user, many=True)

    return Response(serializer.data)
