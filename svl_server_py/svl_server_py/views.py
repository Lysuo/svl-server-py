from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse

from forms import ConnexionForm

def connect(request):
  error = False

  if request.method == "POST":
    form = ConnexionForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data["username"]
      password = form.cleaned_data["password"]
      user = authenticate(username=username, password=password)  

      if user:
        login(request, user)  
      else:
        error = True

    else:
      form = ConnexionForm()

  return render(request, 'signin.html', locals())


def disconnect(request):
  logout(request)
  return redirect(reverse(connect))
