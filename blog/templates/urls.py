
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()), # 클래스명.메서드
    path('<int:pk>/', views.PostDetail.as_view())
    # path('', views.index),
    # path('<int:pk>/', views.single_post_page)
]