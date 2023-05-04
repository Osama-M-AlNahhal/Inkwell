from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserAdminCreationForm, CustomUserCreationForm
from django.core.mail import send_mail

from django.contrib.auth import get_user_model
User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'


def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup')
    return render(request, 'signup.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')