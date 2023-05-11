from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .forms import ReviewForm
from django.http import JsonResponse
import json
import datetime


# --------------------- Main store view
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
         items = []
         order = {'get_cart_total':1, 'get_cart_items':1, 'shipping':False}
         cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

# ---------------------  cartview
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
         items = []
         order = {'get_cart_total':2, 'get_cart_items':2, 'shipping':False}
         cartItems = order['get_cart_items']
         context = {'items': items, 'order': order, 'cartItems': cartItems}
         return render(request, 'store/cart.html', context)

# --------------------- Checkout view
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
         items = []
         order = {'get_cart_total':3, 'get_cart_items':33, 'shipping':False}
         cartItems = order['get_cart_items']
         context = {'items': items, 'order': order, 'cartItems': cartItems}
         return render(request, 'store/checkout.html', context)    

# --------------------- Updateing or delitinf an item view
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        
        orderItem.save()
        
        if orderItem.quantity <= 0:
            orderItem.delete()
    return JsonResponse('Item was added', safe=False)

# --------------------- Order porcecing view
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
            order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		county=data['shipping']['county'],
		eircode=data['shipping']['eircode'],
		)    
    else:
        print("User is not logged in")
        
        return JsonResponse('Payment submitted..', safe=False)
    


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

