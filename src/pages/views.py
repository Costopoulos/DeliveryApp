from django.shortcuts import render
import requests
# Create your views here.
def greeklogin(request):
    # data = {
    #     'username': 'costoswto',
    #     'password': 'nikosklaime'
    # }
    data = {
        'username': 'costo',
        'password': 'Ko$topoulos9'
    }
    token = requests.post('http://localhost:8000/rest-auth/login/', data)
    print(token)
    context = {
        'token': token
    }
    return render(request, "login.html", context)

from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_X_USERNAME')
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })