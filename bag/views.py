from django.shortcuts import render
from store.models import Product



def view_bag(request):

    return render(request, 'bag/bag.html')


