from store.models import Product
from django.contrib import messages
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)



def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']       
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity              
            else:
                bag[item_id]['items_by_size'][size] = quantity
                
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity        


    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        # bag[item_id] += quantity
        bag[item_id]  = quantity
    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']       
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag['item_id']['items_by_size'][size] = quantity
        else:
            del bag['item_id']['items_by_size'][size]
            if not bag['item_id']['items_by_size']:
                bag.pop(item_id)     
    else:
        if quantity > 0:
            bag['item_id'] = quantity
        else:
            bag.pop(item_id)    

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']       
    bag = request.session.get('bag', {})

    if size:       
            del bag['item_id']['items_by_size'][size]
            if not bag['item_id']['items_by_size']:
                bag.pop(item_id)     
    else:
        bag.pop(item_id)        

    request.session['bag'] = bag

    return HttpResponse(status=200)   