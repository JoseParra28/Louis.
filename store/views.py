from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .forms import ReviewForm



def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
         items = []
         order = {'get_cart_total':0, 'get_cart_items':0,}
         context = {'items': items, 'order': order}
         return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
         items = []
         order = {'get_cart_total':0, 'get_cart_items':0,}
         context = {'items': items, 'order': order}
         return render(request, 'store/checkout.html', context)    


def categories(request):
    all_categories = Category.objects.all() 
    return {'all_categories': all_categories}


def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'store/product-info.html', context)



def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products  = Product.objects.filter(category=category)
    return render(request, 'store/category-list.html', {'category': category, 'products': products})


# def add_review(request):
#     return render(request, 'store/add-review.html')


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('store')
    form = ReviewForm()
    ctx = {'form': form}    
    return render(request, 'store/add-review.html', ctx)


def edit_review(request, itemm_id):
    item = get_object_or_404(Comment, id=itemm_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        # return redirect('store')
    form = ReviewForm(instance=item)
    ctx = {'form': form}    
    return render(request, 'store/add-review.html', ctx) 

def delete_item(request, itemm_id):
    item = get_object_or_404(Itemm, id=itemm_id)
    item.delete()
    messages.info(request, 'Your review has been deleted.')
    return redirect('store')      

