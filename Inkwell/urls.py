from django.contrib import admin
from django.urls import path, include
from Inkwell.accounts import views as accounts_views
# from Inkwell.posts.views import HomeView
from Inkwell.posts import views as posts_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', posts_views.home, name='home'),
    path('signup/', accounts_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('signup/', accounts_views.register, name='signup'),
    path('profile/', accounts_views.profile, name='profile'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
