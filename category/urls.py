from django.urls import path
from . import views
urlpatterns=[
    path('fiction/',views.fiction,name='fiction'),
    path('nonfiction/,',views.nonfiction, name='nonfiction'),
    path('science/',views.science,name='science'),
    path('romance/',views.romance,name='romance'),
    path('children/',views.children,name='children'),
    path('mystery/',views.mystery,name='mystery'),

]