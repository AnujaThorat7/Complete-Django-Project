from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/products')
            except:
                pass
    else:
        form = ProductForm()
    return render(request, 'addProduct.html', {'form': form})


def show(request):
    products = Product.objects.all()
    return render(request,"showProduct.html",{'products': products})


def edit(request, id):
    products = Product.objects.get(id=id)
    return render(request, 'edit.html', {'products': products})


def update(request, id):
    products = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance = products)
    if form.is_valid():
        form.save()
        return redirect("/products")
    return render(request, 'edit.html', {'products': products})


def destroy(request, id):
    products = Product.objects.get(id=id)
    products.delete()
    return redirect("/products")

