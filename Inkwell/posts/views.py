from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

"""
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class HomeView(LoginRequiredMixin, ListView):
    Model = Post
    count = User.objects.count()
    template_name = 'home.html'

    def get_queryset(self):
        #Return Posts
        return Post.objects.order_by('created_at')

"""