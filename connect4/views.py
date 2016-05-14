from django.contrib.auth.decorators import login_required
import django.contrib.auth.views as auth_views
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from connect4 import models


# Create your views here.
login = auth_views.login
logout = auth_views.logout


def signup(request):
    """
    write your user sign up view here
    :param request:
    :return:
    """
    pass


@login_required
def games(request):
    """
    Write your view which controls the game set up and selection screen here
    :param request:
    :return:
    """
    pass


@login_required
def play(request):
    """
    write your view which controls the gameplay interaction w the web layer here
    :param request:
    :return:
    """
    pass
