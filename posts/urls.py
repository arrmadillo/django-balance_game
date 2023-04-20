from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_pk>/', views.detail, name='detail'),
    # 주제생성
    path('create/', views.create, name='create'),
    # 선택
    path('<int:post_pk>/select/<str:answer>/', views.select, name='select'),
    # 댓글 작성
    path('<int:post_pk>/comments/', views.comment_create, name='comment_create'),
    # 게시글 좋아요
    path('<int:post_pk>/likes/', views.likes, name="likes"),
]