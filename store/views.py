from .models import *
from django.http import HttpResponse
from .forms import ReviewForm
from .models import *
from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse
from .forms import ReviewForm
from django.contrib import messages
from django.db.models import Q


# --------------------- Main store view
def store(request):
    request.session.set_expiry(0)
    all_products  = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any valid search criteria")
                return render(reverse('products'))

            queries = Q(name_contains=query) | Q(description_contains=query)
            all_products = all_products.filter(queries)   

    context = {
        'all_products': all_products,
        'search_term': query
    }
    
    return render(request, 'store/store.html', context)
    


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



    

