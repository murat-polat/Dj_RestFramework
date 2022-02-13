from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json



@api_view(['GET'])
def RegistertData(request):
    reg_data=requests.get('https://baretest.xyz/api/user/v1/account/registration')
    return Response(reg_data.json())



@api_view(['GET'])
def LoginData(request):
    login_data=requests.get('https://baretest.xyz/api/user/v1/account/login_session')
    return Response(login_data.json())


@api_view([ 'POST'])
def RegisterUser(request):
    url = 'https://baretest.xyz/user_api/v1/account/registration/'

    data = {
        "username": "",
        "email": "",
        "password": "",
        "name": "",
        "terms_of_service": True
    }
    
    response = requests.post(url,data, headers={"Content-Type": "application/x-www-form-urlencoded"})
    return Response(response.json())
