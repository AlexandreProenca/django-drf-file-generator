# coding: utf-8
# Extrator de modelos, este script le o arquivo que esta em core/models.py, extrai as classes e os campos dos modelos
# e gera quatro arquivos: core/urls.py, core/admin.py, core/serializers.py/ core/views.py  
# Autor: Alexandre Proença - linuxloco@gmail.com - alexandre.proenca@hotmail.com.br
# Floripa Dom 18:11 10/05/2015
# !/usr/bin/python
import getopt
import sys
import os
import shutil

MODELS = []

def main(argv):
    '''
    Method main, set output dir and call a specific function, as given in the options
    :param argv:
    :return: None
    '''

    OUTDIR = 'drf_gem_build'

    os.mkdir(OUTDIR) if not os.path.exists(OUTDIR) else OUTDIR

    try:
        myopts, args = getopt.getopt(sys.argv[1:], "m:hcAusavD",
                                     ["help", "clean", "All", "urls", "serializers", "admin", "views"])
    except getopt.GetoptError as e:
        print("\n\033[93mOpsss... "'\033[91m'+str(e))
        help()
        sys.exit(2)

    for o, a in myopts:

        if o == '-m':
            try:
                extractor(a)
            except:
                print("\033[91mInvalid Path!---> \033[93m"+a)
                sys.exit(2)

        elif o in ('-a', '--admin'):
            make_admin(OUTDIR)
            print("\033[91madmin.py genereted at!---> \033[93m" + OUTDIR + "/admin.py")

        elif o in ('-v', '--views'):
            make_views(OUTDIR)
            print("\033[91mviews.py genereted at!---> \033[93m" + OUTDIR + "/views.py")

        elif o in ('-u', '--urls'):
            make_urls(OUTDIR)
            print("\033[91murls.py genereted at!---> \033[93m" + OUTDIR + "/urls.py")

        elif o in ('-s', '--serializers'):
            make_serializers(OUTDIR)
            print("\033[91mserializers.py genereted at!---> \033[93m" + OUTDIR + "/serializers.py")

        elif o in ('-A', '--All'):
            print("\033[91mAll files genereted at!---> \033[93m" + OUTDIR)
            make_urls(OUTDIR)
            make_views(OUTDIR)
            make_admin(OUTDIR)
            make_serializers(OUTDIR)

        elif o in ('-D', '--clean'):
            shutil.rmtree(OUTDIR)
            print("\033[91m"+OUTDIR+" directory was destroyed!!!")

        elif o in ('-h', '--help'):
            help()


def extractor(path):
    '''
    Method receive the models path and extrac Class and fields.
    :param path:
    :return:True if everything went ok
    '''
    f = open(path, "r")
    for line in f:
        if "models.Model" in line:
            MODELS.append({"classe": line.split()[1].split("(")[0]})
            key = line.split()[1].split("(")[0]
        if "models.C" in line or "models.D" in line or "models.F" in line or "models.T" in line or "models.I" in line or "models.O" in line or "models.B" in line:
            MODELS.append({"field": line.split()[0]})
    f.close()


def make_admin(outdir):
    '''
    Method that create the admin.py file where indicated in parameter
    :param outdir:
    :return:True if everything went ok
    '''
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
    '''
    Method that do serializer file from models.py got by extract method, where outdir is indicated
    :param outdir:
    :return:True if everything went ok
    '''
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
    '''
    Method that do urls.py file from models.py got by extract method, where outdir is indicated
    :param outdir:
    :return:True if everything went ok
    '''
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
    '''
    Method that do views.py file from models.py got by extract method, where outdir is indicated
    :param outdir:
    :return:True if everything went ok
    '''
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
    '''
    Method to do a workaround to close ] on files
    :param path:
    :return:True if everything went ok
    '''
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


def help():
    '''
    Method to help users to use command line commands
    :param None:
    :return:None
    '''

    cor = {
    'ROXO' : '\033[95m',
    'AZUL' : '\033[94m',
    'VERDE' : '\033[92m',
    'AMARELO' : '\033[93m',
    'VERMELHO' : '\033[91m',
    'BRANCO' : '\033[0m',
    'BOLD' : '\033[1m',
    'UNDERLINE' : '\033[4m'
    }

    print(cor['VERDE']+"Option:")
    print(cor['AMARELO']+"       -m path/my/models.py  "+cor['BRANCO']+" required parameter, path to models.py file")
    print(cor['AMARELO']+"       -a or --admin         "+cor['BRANCO']+" to create admin.py")
    print(cor['AMARELO']+"       -v or --views          "+cor['BRANCO']+"to create views.py")
    print(cor['AMARELO']+"       -u or --urls           "+cor['BRANCO']+"to create urls.py")
    print(cor['AMARELO']+"       -s or --serializers    "+cor['BRANCO']+"to create serializers.py")
    print(cor['AMARELO']+"       -A or --All            "+cor['BRANCO']+"to create urls.py, admin.py, views.py, serializers.py ")
    print(cor['AMARELO']+"       -D or --clean          "+cor['VERMELHO']+"warning!!! this option will remove gem_build directory and all files inside")
    print(cor['AMARELO']+"       -h or --help           "+cor['BRANCO']+"to show all options")
    print(cor['VERDE']+"Exemples:")
    print(cor['BRANCO']+"      #python drf-gem -a -s -m path/my/models.py")
    print(cor['BRANCO']+"      #python drf-gem -m path/my/models.py --views --serializers")
    print(cor['BRANCO']+"      #python drf-gem -m path/my/models.py --clean")
    print(cor['BRANCO']+"      #python drf-gem -m path/my/models.py --All")

if __name__ == "__main__":
    main(sys.argv[1:])
