from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings, urls


urlpatterns = [
    path('', views.index, name='index'),
    path('donateclicked', views.donateclicked, name='donate'),
    path('funds', views.funds, name='funds'),
    path('add', views.add, name='add'),
    path('home', views.index, name='home'),
]