# coding: utf-8

VIEW_IMPORT = """
# coding: utf-8
from rest_auth.serializers import PasswordResetSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.filters import DjangoFilterBackend
from rest_framework import permissions, viewsets, status, parsers, renderers
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import models
import serializers


"""

VIEW_CLASS_USER = """
class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['username', 'email']

    def get_permissions(self):
        return (AllowAny() if self.request.method == 'POST' else IsAuthenticated()),


"""

VIEW_FINAL = """

class PasswordReset(GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        email = self.request.data['email']

        if not User.objects.filter(email=email):
            return Response(data={"error": "Email " + email + " was not found"}, status=status.HTTP_400_BAD_REQUEST)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        # Return the success message with OK HTTP status
        return Response({"success": "Password reset e-mail has been sent."}, status=status.HTTP_200_OK)

password_reset = PasswordReset.as_view()


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = (AllowAny,)
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    model = Token

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            usuario = User.objects.get(username=request.data[unicode('username')])
            token, created = Token.objects.get_or_create(user=usuario)
            imagem = models.Perfil.objects.filter(usuario=usuario).values('imagem')[0]['imagem']
            serializer = serializers.UserSerializer(usuario)
            return Response(data={"token": token.key, "user": serializer.data, "image": imagem})
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


obtain_auth_token = ObtainAuthToken.as_view()

"""

MODEL_IMPROVE = """

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

#-----------------------------------------------------#
#--------SUPER HACK - DONT TOUCH THIS NEVER-----------#
#-----------------------------------------------------#


def hack_models(length=100):
    from django.contrib.auth.models import User
    username = User._meta.get_field("username")
    username.max_length = length
    hack_validators(username.validators)


def hack_validators(validators, length=100):
    from django.core.validators import MaxLengthValidator
    for key, validator in enumerate(validators):
        if isinstance(validator, MaxLengthValidator):
            validators.pop(key)
    validators.insert(0, MaxLengthValidator(length))

# Seta o max_lenght do username para 100
hack_models(length=100)
"""

URLS_HEAD = """
# coding: utf-8
from django.conf.urls import url, include
from rest_framework import routers
import views


router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'list')
"""

URLS_TAIL = """

urlpatterns = [
    url(r'^', include(router.urls)),
]

"""

SERIALIZERS_HEAD = """
# coding: utf-8
from rest_framework import serializers
import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        write_only_fields = ('password',)

    def update(self, attrs, instance=None):
        user = super(UserSerializer, self).update(attrs, instance)
        user.set_password(attrs['password'])
        return user


"""

ADMIN_HEAD = """
# coding: utf-8
from django.contrib import admin
import models

"""
