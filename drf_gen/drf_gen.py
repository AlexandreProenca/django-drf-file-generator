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


MODELS = []


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

    extractor(args.models_path)

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
        op = raw_input('\033[91m Warning!!! '+outputdir+'directory will be destroyed!!! do you have sure? yes|not''\033[0m')
        if op == 'yes':
            shutil.rmtree(outputdir)
            if args.verbose:
                print('\033[91m'+outputdir+' directory was destroyed!!!''\033[0m')
        else:
            print("OK nothing was destroyed.")
            sys.exit(0)

def extractor(path):
    """
    Method receive the models path and extrac Class and fields.
    :param path:
    :return:True if everything went ok
    """
    f = open(path, "r")
    for line in f:
        if "models.Model" in line:
            MODELS.append({"classe": line.split()[1].split("(")[0]})
        if "models.C" in line or "models.D" in line or "models.F" in line or "models.T" in line or "models.I" in \
                line or "models.O" in line or "models.B" in line:
            MODELS.append({"field": line.split()[0]})
    f.close()
    return True


def make_admin(outdir):
    """
    Method that create the admin.py file where indicated in parameter
    :param outdir:
    :return:True if everything went ok
    """
    f = open(outdir + "/admin.py", 'w')
    f.write("# coding: utf-8" + '\n')
    f.write("from django.contrib import admin" + '\n')
    f.write("import models" + '\n')
    f.write("" + '\n')
    for line in MODELS:

        if "classe" in line:
            f.write('\n' + "class " + line['classe'] + "(admin.ModelAdmin):" + '\n')
            f.write("    list_display = ['id'")
        if "field" in line:
            f.write(", " + "'" + line['field'] + "'")

    f.write("" + '\n')
    f.write("" + '\n')
    for line in MODELS:
        if "classe" in line:
            f.write("admin.site.register(models." + line['classe'] + ", " + line['classe'] + ")" '\n')
    f.close()
    close_cap(outdir + "/admin.py")
    return True


def make_serializers(outdir):
    """
    Method that do serializer file from models.py got by extract method, where outdir is indicated
    :param outdir:
    :return:True if everything went ok
    """
    f = open(outdir + "/serializers.py", 'w')
    f.write("# coding: utf-8" + '\n')
    f.write("from rest_framework import serializers" + '\n')
    f.write("import models" + '\n')
    f.write("from django.contrib.auth.models import User" + '\n')
    f.write("" + '\n')
    f.write("" + '\n')
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
    f.write("" + '\n')
    for line in MODELS:
        if "classe" in line:
            f.write('\n' + "class " + line['classe'] + "Serializer" + "(serializers.ModelSerializer):" + '\n')
            f.write("    class Meta:" + '\n')
            f.write("        model = models." + line['classe'] + '\n')
    f.close()
    return True


def make_urls(outdir):
    """
    Method that do urls.py file from models.py got by extract method, where outdir is indicated
    :param outdir:
    :return:True if everything went ok
    """
    f = open(outdir + "/urls.py", 'w')
    f.write("# coding: utf-8" + '\n')
    f.write("from django.conf.urls import patterns, url, include" + '\n')
    f.write("from rest_framework.urlpatterns import format_suffix_patterns" + '\n')
    f.write("from rest_framework import routers" + '\n')
    f.write("import views" + '\n')
    f.write("" + '\n')
    f.write("router = routers.DefaultRouter()" + '\n')
    f.write("router.register(r'users', views.UserView, 'list')" + '\n')
    for line in MODELS:
        if "classe" in line:
            f.write(
                "router.register(r'" + line['classe'].lower() + "s', views." + line['classe'] + "View, 'list')" + '\n')
    f.write("" + '\n')
    f.write("urlpatterns = patterns('',)" + '\n')
    f.write("" + '\n')
    f.write("urlpatterns = format_suffix_patterns(urlpatterns)" + '\n')
    f.write("" + '\n')
    f.write("urlpatterns += patterns('', url(r'^', include(router.urls)),)" + '\n')
    f.close()
    return True


def make_views(outdir):
    """
    Method that do views.py file from models.py got by extract method, where outdir is indicated
    :param outdir:
    :return:True if everything went ok
    """
    f = open(outdir + "/views.py", 'w')
    f.write("# coding: utf-8" + '\n')
    f.write("from rest_framework.filters import DjangoFilterBackend" + '\n')
    f.write("from rest_framework import viewsets" + '\n')
    f.write("from django.contrib.auth.models import User" + '\n')
    f.write("import models" + '\n')
    f.write("import serializers" + '\n')
    f.write("" + '\n')
    f.write("" + '\n')
    f.write("class UserView(viewsets.ModelViewSet):" + '\n')
    f.write("    serializer_class = serializers.UserSerializer" + '\n')
    f.write("    queryset = User.objects.all()" + '\n')
    f.write("    filter_backends = [DjangoFilterBackend" + '\n')
    f.write("    filter_fields = ['username', 'email'")
    for line in MODELS:
        if "classe" in line:
            f.write("" + '\n')
            f.write('\n' + "class " + line['classe'] + "View" + "(viewsets.ModelViewSet):" + '\n')
            f.write("    serializer_class = serializers." + line['classe'] + "Serializer" + '\n')
            f.write("    queryset = models." + line['classe'] + ".objects.all()" + '\n')
            f.write("    filter_backends = [DjangoFilterBackend" + '\n')
            f.write("    filter_fields = ['id'")
        if "field" in line:
            f.write(", " + "'" + line['field'] + "'")

    f.close()
    close_cap(outdir + "/views.py")
    return True


def close_cap(path):
    """
    Method to do a workaround to close ] on files
    :param path:
    :return:True if everything went ok
    """
    arr = []
    arr_new = []
    f = open(path, "r")
    [arr.append(line.strip()) for line in f]
    f.close()
    for l in arr:
        if '[' in l:
            arr_new.append("    " + l + ']\n')
        elif 'serializer_class' in l or 'queryset' in l:
            arr_new.append("    " + l)
        else:
            arr_new.append(l)

    f = open(path, "w")
    [f.write(line + '\n') for line in arr_new]
    f.close()
    return True


if __name__ == "__main__":
    main()