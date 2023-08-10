from django.shortcuts import render, redirect

from item.models import Category, Item

# Create your views here.
from .forms import SignupForm


def index(request):
    # GET all items WHERE sold = False, return only items 0 THROUGH 6
    items = Item.objects.filter(is_sold=False)[0:6]
    # GET all categories
    categories = Category.objects.all()

    # render page passing in 'categories' & 'items' data
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    # if method is POST
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        # if NOT POST, return the signup form again
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
