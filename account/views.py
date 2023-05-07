from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.sites.shortcuts import get_current_site
from .token import user_tokenizer_generate
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode



def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('store')

    context = {'form': form}
    return render(request, 'account/registration/register.html', context)


def email_verification(request):
    pass

def email_verification_sent(request):
    pass

def email_verification_success(request):
    pass

def email_verification_failed(request):
    pass
