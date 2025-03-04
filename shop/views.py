from django.shortcuts import render,redirect,HttpResponse
from .models import Category,Products
from django.contrib import messages
from shop.form import CustomUserForm

# Create your views here.
def home(request):
     products = Products.objects.filter(trending=1)
     return render(request, "shop/index.html",{"products":products})

def register(request):
    form=CustomUserForm()
    return render(request, "shop/register.html",{'form':form})

def login(request):
    return render(request, "shop/login.html")

def collection(request):
    category = Category.objects.filter(status=0)  # Renamed variable for consistency
    return render(request, "shop/collection.html", {"category": category})  # Updated context key

def collectionview(request, name):
    if Category.objects.filter(name=name, status=0).exists():
        products = Products.objects.filter(category__name=name)  # Fixed the filter
        return render(request, "shop/products/index.html", {"products": products,"category_name":name})
    else:
        messages.warning(request, "No such category found")
        return redirect("collection")



def product_details(request, cname, pname):
    if Category.objects.filter(name=cname, status=0).exists():
        product = Products.objects.filter(name=pname, status=0).first()
        if product:
            return render(request, "shop/products/product_details.html", {"products": product})
        else:
            messages.error(request, "No such product found")
            return redirect("collection")  
    else:
        messages.error(request, "No such category found")
        return redirect("collection")
