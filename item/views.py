from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Category, Item


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) |
                             Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })


def detail(request, pk):
    # retrieve an object from DB
    item = get_object_or_404(Item, pk=pk)
    # 3 items WHERE category matches,
    related_items = Item.objects.filter(
        category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })


# add items based on form component
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            # save form info to database
            item = form.save(commit=False)
            # associate logged in user with item
            item.createdBy = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        # generate a new form if not completely filled in
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item'
    })


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, createdBy=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            # save form info to database
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        # generate a new form if not completely filled in
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item'
    })


@login_required
def delete(request, pk):
    # delete a specific item
    item = get_object_or_404(Item, pk=pk, createdBy=request.user)
    item.delete()

    return redirect('dashboard:index')
