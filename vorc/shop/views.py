from django.shortcuts import render
from shop.models import User

def shop(request):
    context = {"name_page": "shop"}
    return render(request, "shop.html", context)

def shopDetail(request):
    context = {"name_page": "shop detail"}
    return render(request, "shop_detail.html", context)

def cart(request):
    context = {"name_page": "cart"}
    return render(request, "cart.html", context)

def checkout(request):
    context = {"name_page": "checkout"}
    return render(request, "checkout.html", context)

def myAccount(request):
    context = {"name_page": "my account"}
    return render(request, "my_account.html", context)

def wishlist(request):
    context = {"name_page": "wishlist"}
    return render(request, "wishlist.html", context)

#apple_record = Items(name = "Apple", items_group = "FR", price = "9.45$ for 1(kg)")
#apple_record.save()