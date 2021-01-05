from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .forms import LinkGenerateForm
from .shorty import generate_short_url
from .models import URL
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse

# Create your views here.

def home_view(request):
    form = LinkGenerateForm(request.POST or None)
    if form.is_valid():
        long_url = form.cleaned_data['long_url']
        short_url = generate_short_url()
        m = URL(short_url=short_url, long_url=long_url)
        m.save()
        form = LinkGenerateForm()
        return redirect('success-view', short_url=short_url)
    context = {
        'form' : form
    }
    return render(request, 'index.html', context)

def redirector(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    url.clicks += 1
    url.save()
    return redirect(url.long_url)

def success_view(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    host = HttpRequest.get_host(request)
    context = {
        'data' : url,
        'host' : host,
    }
    return render(request, 'success.html', context)

def register(request):
    if request.method == "GET":
        return render(request, 'registration/register.html', {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))