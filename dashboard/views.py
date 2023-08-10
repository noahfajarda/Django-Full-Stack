from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from item.models import Item


@login_required
def index(request):
    # retrieve all user-created items
    items = Item.objects.filter(createdBy=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })
