from django.shortcuts import render, redirect, get_object_or_404
from .forms import LinkGenerateForm
from .shorty import generate_short_url
from .models import URL

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
    context = {
        'data' : url,
    }
    return render(request, 'success.html', context)