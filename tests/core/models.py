# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    repositorio = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'projeto'

    def __unicode__(self):
        return self.nome


class Tags(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'tags'

    def __unicode__(self):
        return self.nome


class StatusHttp(models.Model):
    codigo = models.CharField(max_length=4)
    tipo = models.CharField(max_length=25)
    descricao = models.TextField()

    class Meta:
        managed = True
        db_table = 'status_http'

    def __unicode__(self):
        return self.codigo


class Endpoint(models.Model):
    path = models.CharField(max_length=100)
    metodo = models.CharField(max_length=6) #ENUM (GET,POST,PUT,DELETE,PATCH)
    saida = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField( blank=True, null=True)
    solicitante = models.OneToOneField(User)
    executor = models.OneToOneField(User)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    projeto = models.ForeignKey(Projeto)
    tag = models.ForeignKey(Tags)
    status_http_erro = models.ForeignKey(StatusHttp)
    mensagem_erro = models.CharField(max_length=255)
    mensagem_sucesso = models.CharField(max_length=255)
    status_http_sucesso = models.ForeignKey(StatusHttp)

    class Meta:
        managed = True
        db_table = 'endpoint'

    def __unicode__(self):
        return self.path


class Entrada(models.Model):
    chave = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    endpoint = models.ForeignKey(Endpoint)

    class Meta:
        managed = True
        db_table = 'entrada'

    def __unicode__(self):
        return "parametros de entrada"



class Comentario(models.Model):
    comentario = models.TextField()
    like = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User)
    endpoint = models.ForeignKey(Endpoint)

    class Meta:
        managed = True
        db_table = 'comentario'

    def __unicode__(self):
        return self.endpoint.path



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

#Seta o max_lenght do username para 100
hack_models(length=100)
#-----------------------------------------------------#
