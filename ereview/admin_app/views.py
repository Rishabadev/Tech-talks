from django.shortcuts import render,redirect, get_object_or_404
from .forms import ProductForm , AdminRegistrationForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import Product,Review
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm

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
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        product.delete()
        return redirect('admin_product_list')

    return render(request, 'admin_app/delete_confirmation.html', {'product': product})

@staff_member_required
def admin_product_list(request):
    products=Product.objects.all()
    return render(request, 'admin_app/admin_product_list.html',{'products':products})

@staff_member_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return HttpResponseRedirect(reverse('admin_review_list'))
    

@staff_member_required
def admin_dashboard(request):
    total_products = Product.objects.count()
    total_reviews = Review.objects.count()
    latest_products = Product.objects.order_by('-id')[:5]
    latest_reviews = Review.objects.order_by('-id')[:5]

    context = {
        'total_products': total_products,
        'total_reviews': total_reviews,
        'latest_products': latest_products,
        'latest_reviews': latest_reviews,
    }
    return render(request, 'admin_app/admin_dashboard.html', context)

@staff_member_required
def admin_review_list(request):
    reviews = Review.objects.all()
    return render(request, 'admin_app/admin_review_list.html', {'reviews': reviews})

@staff_member_required
def admin_delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect(reverse('admin_review_list'))


def home(request):
    return render(request, 'admin_app/home.html')

from django.contrib.auth.views import LoginView

class AdminLoginView(LoginView):
    template_name = 'admin_app/admin_login.html'  



def admin_registration(request):
    if request.method == "POST":
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect(reverse('admin_dashboard'))  
    else:
        form = AdminRegistrationForm()
    return render(request, "admin_app/admin_registration.html", {"form": form})


def admin_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:  
                login(request, user)
                return redirect(reverse('admin_dashboard'))  
            else:
                form.add_error(None, "You are not authorized as an admin.")
    else:
        form = AuthenticationForm()
    
    return render(request, "admin_app/admin_login.html", {"form": form})

def admin_logout(request):
    logout(request)
    return redirect(reverse('admin_login'))  