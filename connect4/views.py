from django.contrib.auth.decorators import login_required
import django.contrib.auth.views as auth_views
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from connect4 import models
from connect4.forms import UserSignupForm

# Create your views here.
login = auth_views.login
logout = auth_views.logout


signup = CreateView.as_view(
    form_class=UserSignupForm,
    template_name='registration/signup.html',
    success_url=reverse_lazy('home'),
)


@login_required
def games(request):
    """
    Write your view which controls the game set up and selection screen here
    :param request:
    :return:
    """
    games = models.Game.games_for_user(request.user)
    return render(request, 'games.html', { 'games': games })


@login_required
def play(request):
    """
    write your view which controls the gameplay interaction w the web layer here
    :param request:
    :return:
    """
    pass
