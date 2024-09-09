from django.urls import path
from . import views
urlpatterns=[
    path('home/', views.home ,name='home'),
    path('rent/', views.rent ,name='rent'),
    path('', views.index ,name='index'),
    path('login/', views.login ,name='login'),
    path('sell/', views.sell ,name='sell'),
    path('shop/', views.shop ,name='shop'),

]