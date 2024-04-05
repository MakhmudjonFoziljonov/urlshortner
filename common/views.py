from django.shortcuts import render, redirect
from .models import Url


# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        original_url = request.POST['original_url']
        url = Url.objects.create(original_url=original_url)
        short_url = request.build_absolute_uri('/') + url.short_code
        context['short_url'] = short_url

    return render(request, 'index.html', context)


def redirect_to_original(request, short_code):
    url = Url.objects.get(short_code=short_code)
    return redirect(url.original_url)
