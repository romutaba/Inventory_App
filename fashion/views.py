from django.shortcuts import render
from django.http import Http404

from .models import Items


def index(request):
    item = Items.objects.exclude(units=0)
    return render(request, 'fashion/index.html', {
        'items': item,
    })
    #return HttpResponse('<p>In index view</p>')

def item_detail(request, id):
    try:
        item = Items.objects.get(id=id)
    except Items.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'fashion/item_detail.html', {
        'items': item,
    })
