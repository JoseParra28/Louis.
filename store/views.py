from django.shortcuts import render
from .models import Category, Product



def store(request):
    return render(request, 'store/store.html')


def categories(request):
    all_categories = Category.objects.all()
    context = {'all_categories': all_categories}   
    return render(request, 'store/store.html', context)


def pie(request):
    # request.session.set_expiry(0)
    pies = Pie.objects.all()
    ctx = {'pies': pies}
    print(pies)
    return render(request, "food/pies.html", ctx)