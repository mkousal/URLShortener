from django.shortcuts import render, redirect
from .forms import LinkGenerateForm
from .shorty import create_short_url

# Create your views here.

def home_view(request):
    form = LinkGenerateForm(request.POST or None)
    if form.is_valid():
        long_url = form.cleaned_data['long_url']
        create_short_url(long_url)
        # form = LinkGenerateForm()
    context = {
        'form' : form
    }
    return render(request, 'index.html', context)