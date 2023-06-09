from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
    return redirect(reverse('store'))
    # return render(request, 'checkout/checkout.html')

    order_from = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_from': order_from,
    }
    return render(request, template, context)
    # return render(request, 'checkout/checkout.html')