from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),

    path('register/',views.register,name='register'),
    path('base/',views.base, name='base'),
    path('sermons/', views.sermons_view, name='sermons'),
    path('inspiration/<str:theme>/', views.sermons_view, name='inspiration'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('daily-verse/', views.get_daily_verse, name='daily_verse'),
    path('devotional/<int:pk>/', views.devotional_detail, name='devotional_detail'),
    path('events/', views.events, name='events'),  # your existing view for events
    



]
 