from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_pk>/', views.detail, name='detail'),

]