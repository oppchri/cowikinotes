from wiki import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('page/<str:page_name>/', views.page, name='page'),
    path('category/<str:category_name>/', views.category, name='category'),
] 