# coding: utf-8
# Extrator de modelos, este programa le o arquivo um arquivo no padrão django models.py, extrai as classes e os
# campos dos modelos e e opçionalmente pode gera quatro arquivos: urls.py, admin.py, serializers.py e views.py
# Autor: Alexandre Proença - linuxloco@gmail.com - alexandre.proenca@hotmail.com.br
# Floripa Dom 18:11 10/05/2015
# !/usr/bin/python
from ConfigParser import RawConfigParser
from argparse import ArgumentParser
from pkg_resources import resource_stream
import config
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
    config.readfp(resource_stream('drf_gen', 'config.ini'))

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

    models = extractor_obj(args.models_path)
    if models:
        if args.admin:
            make_admin(outputdir)
            if args.verbose:
                print("\033[91madmin.py genereted at!---> \033[93m" + outputdir + "/admin.py")

        if args.views:
            make_views(outputdir)
            if args.verbose:
                print("\033[91mviews.py genereted at!---> \033[93m" + outputdir + "/views.py")

        if args.urls:
            make_urls(outputdir)
            if args.verbose:
                print("\033[91murls.py genereted at!---> \033[93m" + outputdir + "/urls.py")

        if args.serializers:
            make_serializers(outputdir)
            if args.verbose:
                print("\033[91serializers.py genereted at!---> \033[93m" + outputdir + "/serializers.py")

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

        if args.Delete:
            op = raw_input('\033[91m Warning!!! '+outputdir+'directory will be destroyed!!! do you have sure? yes|not ''\033[0m')
            if op == 'yes':
                shutil.rmtree(outputdir)
                if args.verbose:
                    print('\033[91m'+outputdir+' directory was destroyed!!!''\033[0m')
                    sys.exit(0)
            else:
                print("OK nothing was destroyed.")
                sys.exit(0)

        make_models_improve()
        sys.exit(0)
    else:
        print("can't read models.py, make sure that you was used a valid path/file.")
        sys.exit(1)


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
        f.write(config.ADMIN_HEAD)
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
        f.write(config.SERIALIZERS_HEAD)
        for obj in OBJ_ARR:
            f.write('\n' + "class {}Serializer(serializers.ModelSerializer):".format(obj.name) + '\n')
            f.write("    class Meta:" + '\n')
            f.write("        model = models.{}".format(obj.name) + '\n')
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
        f.write(config.URLS_HEAD)
        for obj in OBJ_ARR:
            f.write("router.register(r'" + obj.name.lower() + "s', views." + obj.name + "View, 'list')" + '\n')
        f.write(config.URLS_TAIL)
    return True


def make_views(outdir):
    """
    Method that do views.py file from models.py got by extract method, where outdir is indicated
    :param outdir:
    :return:True if everything went ok
    """
    with open(outdir + "/views.py", 'w') as f:
        f.write(config.VIEW_IMPORT)
        f.write(config.VIEW_CLASS_USER)

        for obj in OBJ_ARR:
            f.write("" + '\n')
            f.write('\n' + "class " + obj.name + "View" + "(viewsets.ModelViewSet):" + '\n')
            f.write("    serializer_class = serializers." + obj.name + "Serializer" + '\n')
            f.write("    queryset = models." + obj.name + ".objects.all()" + '\n')
            f.write("    filter_backends = [DjangoFilterBackend]" + '\n')
            f.write("    filter_fields = {}".format(obj.fields))
            f.write("" + '\n')

        f.write(config.VIEW_FINAL)
    return True


def make_models_improve():
    with open("core/models.py", 'a') as f:
        f.write(config.MODEL_IMPROVE)


if __name__ == "__main__":
    main()