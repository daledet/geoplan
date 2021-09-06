from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculator', views.index, name='calculator'),
    path('add', views.addition, name='add'),
    path('sub', views.subtraction, name='sub'),
    path('multi', views.multiplication, name='multi'),
    path('div', views.division, name='div'),
    path('project', views.project, name='project')
]
