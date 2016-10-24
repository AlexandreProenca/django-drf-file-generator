# coding: utf-8
# Extrator de modelos, este programa le o arquivo um arquivo no padrão django models.py, extrai as classes e os
# campos dos modelos e e opçionalmente pode gera quatro arquivos: urls.py, admin.py, serializers.py e views.py
# Autor: Alexandre Proença - linuxloco@gmail.com - alexandre.proenca@hotmail.com.br
# Floripa Dom 18:11 10/05/2015
# !/usr/bin/python
from ConfigParser import RawConfigParser
from argparse import ArgumentParser
from pkg_resources import resource_stream

import sys
import os
import shutil


OBJ_ARR = []


class Obj(object):
    def __init__(self, name=None, fields=[]):
        self.name = name
        self.fields = fields


def main():
    """
    Method main, set output dir and call a specific function, as given in the options
    :param argv:
    :return: None
    """
    config = RawConfigParser()
    config.readfp(resource_stream('drf_gen','config.ini'))

    outputdir = config.get('outputdir', 'dir')
    os.mkdir(outputdir) if not os.path.exists(outputdir) else outputdir

    ap = ArgumentParser()
    ap.add_argument('-vv', '--verbose',
                    default=False,
                    help='Increase verbosity.')

    ap.add_argument('-m', '--model',
                    required=True,
                    action='store',
                    dest='models_path',
                    help='Path to your models.py file.')

    ap.add_argument('-a', '--admin',
                    action='store_true',
                    help='Will create a admin.py file from your models.py.')

    ap.add_argument('-v', '--views',
                    action='store_true',
                    help='Will create a views.py file from your models.py.')

    ap.add_argument('-s', '--serializers',
                    action='store_true',
                    help='Will create a serializers.py file from your models.py.')

    ap.add_argument('-u', '--urls',
                    action='store_true',
                    help='Will create a urls.py file from your models.py.')

    ap.add_argument('-A', '--All',
                    action='store_true',
                    help='Will create four files: urls.py, admin.py, views.py, serializers.py, from your models.py.')

    ap.add_argument('-D', '--Delete',
                    action='store_true',
                    help='\033[91m'+outputdir+' directory will be destroyed!!!''\033[0m')

    args = ap.parse_args()

    extractor_obj(args.models_path)

    if args.admin:
        make_admin(outputdir)
        if args.verbose:
            print("\033[91madmin.py genereted at!---> \033[93m" + outputdir + "/admin.py")
            sys.exit(0)

    if args.views:
        make_views(outputdir)
        if args.verbose:
            print("\033[91mviews.py genereted at!---> \033[93m" + outputdir + "/views.py")
            sys.exit(0)

    if args.urls:
        make_urls(outputdir)
        if args.verbose:
            print("\033[91murls.py genereted at!---> \033[93m" + outputdir + "/urls.py")
            sys.exit(0)

    if args.serializers:
        make_serializers(outputdir)
        if args.verbose:
            print("\033[91serializers.py genereted at!---> \033[93m" + outputdir + "/serializers.py")
            sys.exit(0)

    if args.All:
        make_admin(outputdir)
        make_views(outputdir)
        make_urls(outputdir)
        make_serializers(outputdir)
        if args.verbose:
            print("\033[91madmin.py genereted at!---> \033[93m" + outputdir + "/admin.py")
            print("\033[91mviews.py genereted at!---> \033[93m" + outputdir + "/views.py")
            print("\033[91murls.py genereted at!---> \033[93m" + outputdir + "/urls.py")
            print("\033[91serializers.py genereted at!---> \033[93m" + outputdir + "/serializers.py")
            sys.exit(0)

    if args.Delete:
        op = raw_input('\033[91m Warning!!! '+outputdir+'directory will be destroyed!!! do you have sure? yes|not ''\033[0m')
        if op == 'yes':
            shutil.rmtree(outputdir)
            if args.verbose:
                print('\033[91m'+outputdir+' directory was destroyed!!!''\033[0m')
        else:
            print("OK nothing was destroyed.")
            sys.exit(0)

    make_models_improve()
    make_views_improve()


def extractor_obj(path):
    """
    Method receive the models path and extrac Class and fields.
    :param path:
    :return:True if everything went ok
    """
    with open(path, "r") as f:
        for line in f:
            if "models.Model" in line:
                obj = Obj(name=line.split()[1].split("(")[0], fields=[])
                OBJ_ARR.append(obj)
            if "models.A" in line \
                    or "models.B" in line \
                    or "models.C" in line \
                    or "models.D" in line \
                    or "models.E" in line \
                    or "models.F" in line \
                    or "models.I" in line \
                    or "models.G" in line \
                    or "models.N" in line \
                    or "models.P" in line \
                    or "models.S" in line \
                    or "models.T" in line \
                    or "models.U" in line \
                    or "models.O" in line:

                if OBJ_ARR > 0:
                    OBJ_ARR[-1].fields.append(line.split()[0])
    return True


def make_admin(outdir):
    """
    Method that create the admin.py file where indicated in parameter
    :param outdir:
    :return:True if everything went ok
    """
    with open(outdir + "/admin.py", 'w') as f:
        f.write("# coding: utf-8" + '\n')
        f.write("from django.contrib import admin" + '\n')
        f.write("import models" + '\n')
        f.write("" + '\n')
        for obj in OBJ_ARR:
            f.write('\n' + "class {}(admin.ModelAdmin):".format(obj.name) + '\n')
            f.write("    list_display = {}".format(obj.fields))
            f.write("" + '\n\n')

        for obj in OBJ_ARR:
            f.write("admin.site.register(models.{0}, {0})".format(obj.name) + '\n')

    return True


def make_serializers(outdir):
    """
    Method that do serializer file from models.py got by extract method, where outdir is indicated
    :param outdir:
    :return:True if everything went ok
    """
    with open(outdir + "/serializers.py", 'w') as f:
        f.write("# coding: utf-8" + '\n')
        f.write("from rest_framework import serializers" + '\n')
        f.write("import models" + '\n')
        f.write("from django.contrib.auth.models import User" + '\n')
        f.write("" + '\n\n')
        f.write("class UserSerializer(serializers.ModelSerializer):" + '\n')
        f.write("    class Meta:" + '\n')
        f.write("        model = User" + '\n')
        f.write("        fields = ('id', 'username', 'email', 'password')" + '\n')
        f.write("        write_only_fields = ('password',)" + '\n')
        f.write("" + '\n')
        f.write("    def update(self, attrs, instance=None):" + '\n')
        f.write("        user = super(UserSerializer, self).update(attrs, instance)" + '\n')
        f.write("        user.set_password(attrs['password'])" + '\n')
        f.write("        return user" + '\n')
        f.write("" + '\n')

        for obj in OBJ_ARR:
            f.write('\n' + "class {}Serializer(serializers.ModelSerializer):".format(obj.name) + '\n')
            f.write("    class Meta:" + '\n')
            f.write("        model = models.{}".format(obj.name) + '\n\n')
            f.write("        fields = {}".format(tuple(obj.fields)) + '\n\n')

    return True


def make_urls(outdir):
    """
    Method that do urls.py file from models.py got by extract method, where outdir is indicated
    :param outdir:
    # coding: utf-8
    :return:True if everything went ok
    """
    with open(outdir + "/urls.py", 'w') as f:
        f.write("# coding: utf-8" + '\n')
        f.write("from django.conf.urls import url, include" + '\n')
        f.write("from rest_framework import routers" + '\n')
        f.write("import views" + '\n')
        f.write("" + '\n')
        f.write("router = routers.DefaultRouter()" + '\n')
        f.write("router.register(r'users', views.UserView, 'list')" + '\n')
        for obj in OBJ_ARR:
            f.write("router.register(r'" + obj.name.lower() + "s', views." + obj.name + "View, 'list')" + '\n')
        f.write("" + '\n')
        f.write("urlpatterns = [" + '\n')
        f.write("    url(r'^', include(router.urls))," + '\n')
        f.write("]" + '\n')
    return True


def make_views(outdir):
    """
    Method that do views.py file from models.py got by extract method, where outdir is indicated
    :param outdir:
    :return:True if everything went ok
    """
    with open(outdir + "/views.py", 'w') as f:
        f.write("# coding: utf-8" + '\n')
        f.write("from rest_framework.filters import DjangoFilterBackend" + '\n')
        f.write("from rest_framework import viewsets" + '\n')
        f.write("from django.contrib.auth.models import User" + '\n')
        f.write("import models" + '\n')
        f.write("import serializers" + '\n')
        f.write("" + '\n\n')
        f.write("class UserView(viewsets.ModelViewSet):" + '\n')
        f.write("    serializer_class = serializers.UserSerializer" + '\n')
        f.write("    queryset = User.objects.all()" + '\n')
        f.write("    filter_backends = [DjangoFilterBackend]" + '\n')
        f.write("    filter_fields = ['username', 'email']")
        f.write("" + '\n')

        for obj in OBJ_ARR:
            f.write("" + '\n')
            f.write('\n' + "class " + obj.name + "View" + "(viewsets.ModelViewSet):" + '\n')
            f.write("    serializer_class = serializers." + obj.name + "Serializer" + '\n')
            f.write("    queryset = models." + obj.name + ".objects.all()" + '\n')
            f.write("    filter_backends = [DjangoFilterBackend]" + '\n')
            f.write("    filter_fields = {}".format(obj.fields))
            f.write("" + '\n')

    return True


def make_models_improve():
    with open("core/models.py", 'a') as f:
        f.write("""

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
)


def make_views_improve():
    with open("core/views.py", 'a') as f:
        f.write("""

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
)


if __name__ == "__main__":
    main()