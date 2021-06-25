from django.urls import path
from shop import views
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path("shop/", views.shop, name="shop_page"),
    path("shop_detail/", views.shopDetail, name="shop_detail_page"),
    path("cart/", views.cart, name="cart_page"),
    path("checkout/", views.checkout, name="checkout_page"),
    path("my_account/", views.myAccount, name="my_account_page"),
    path("wishlist/", views.wishlist, name="wishlist_page"),
]