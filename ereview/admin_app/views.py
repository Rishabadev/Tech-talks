from django.shortcuts import render,redirect, get_object_or_404
from .forms import ProductForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import Product
from django.http import HttpResponseRedirect
from django.urls import reverse

@staff_member_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductForm()
    return render(request, 'admin_app/add_product.html',{'form':form})

@staff_member_required
def edit_product(request, product_id):
    product = get_object_or_404(Product , id=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'admin_app/edit_product.html',{'form':form, 'product':product})

@staff_member_required
def delete_product(request, product_id):
    product = get_object_or_404(product, id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('admin_product_list'))

@staff_member_required
def admin_product_list(request):
    products=Product.objects.all()
    return render(request, 'admin_app/admin_product_ist.html',{'products':products})

    