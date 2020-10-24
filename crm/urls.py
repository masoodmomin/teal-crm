from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="home"),
    path('products/', views.products, name="products"),
    path('create_product/', views.create_product, name="create_product"),
    path('update_product/<str:pk>/', views.update_product, name="update_product"),
    path('delete_product/<str:pk>/', views.delete_product, name="delete_product"),
    path('orders/', views.orders, name="orders"),
    path('contacts/', views.contacts, name="contacts"),
    path('delete_contact/<str:pk>/', views.delete_contact, name="delete_contact"),
    path('update_contact/<str:pk>/', views.update_contact, name="update_contact"),
    path('add_contact/', views.add_contact, name="add_contact"),
    path('customer_orders/<str:pk>/', views.customer_orders, name="customer_orders"),
    path('create_order/', views.create_order, name="create_order"),
    path('update_order/<str:pk>', views.update_order, name="update_order"),
    path('delete_order/<str:pk>', views.delete_order, name="delete_order"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout")
]
