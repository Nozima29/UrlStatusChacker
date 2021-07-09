from django.shortcuts import render
from .models import UrlModel
import requests

# Create your views here.

def index(request):
    template = 'index.html'
    urls = UrlModel.objects.all()
    for u in urls:
        try:
            url = requests.head(u.url)
            u.status_code = url.status_code
            u.save()
        except:
            pass

    if request.is_ajax():
        update_urls = request.GET.getlist('urls[]')
        for url in update_urls:
            new_url = requests.head(url)
            u = urls.get(url=url)
            u.status_code = new_url.status_code
            u.save()

    context = {'urls': urls}

    return render(request, template, context)
