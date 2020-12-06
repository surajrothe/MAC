from django.urls import path, include
from. import views

app_name = "shop"

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('tracker/', views.tracker, name='tracker'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search, name='search'),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("home/handlerequest/", views.handlerequest, name="handlerequest"),
]