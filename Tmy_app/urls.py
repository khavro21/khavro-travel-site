from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PostListView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.home, name='home'),
    path('city/', views.SearchView.as_view(), name='city'),
    path('detail/<int:city_id>', views.detail, name='detail'),
    path('contacts', views.contacts, name='contacts'),
    path('about_us', views.about_us, name='about_us'),

    # Users
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('login', auth_views.LoginView.as_view(template_name='Tmy_app/users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='Tmy_app/users/logout.html'), name='logout'),
    path('feedback_page', PostListView.as_view(), name='feedback_page'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
