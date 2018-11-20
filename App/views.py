# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from WorkForce import Parser

# Create your views here.

def index(request):
    parser = Parser()
    return HttpResponse(parser.ReturnText())

def db(request):
    parser = Parser()
    parser.SaveToDb()
    return HttpResponse('<h1>Done<h1>')

def retrieve(request):
    parser = Parser()
    return HttpResponse(parser.RetrieveFromDb())

def dumpJson(request):
    parser = Parser()
    return HttpResponse(parser.ExtractDbToFile())