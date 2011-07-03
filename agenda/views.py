#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import ItemAgenda


def index(resquest):
    return HttpResponse('Olá mundo')


def lista(request):
    lista_itens = ItemAgenda.objects.all()
    return render_to_response("lista.html", {'lista_item' : lista_itens})

