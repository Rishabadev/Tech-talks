from django.shortcuts import render,redirect, get_object_or_404
from .forms import ProductForm , AdminRegistrationForm
from .models import Product,Review

from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.groups.filter(name='Admin').exists()
       
@user_passes_test(is_admin)
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductForm()
    return render(request, 'admin_app/add_product.html',{'form':form})

@user_passes_test(is_admin)
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
@user_passes_test(is_admin)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        product.delete()
        return redirect('admin_product_list')

    return render(request, 'admin_app/delete_confirmation.html', {'product': product})

@user_passes_test(is_admin)
def admin_product_list(request):
    products=Product.objects.all()
    return render(request, 'admin_app/admin_product_list.html',{'products':products})

    

@user_passes_test(is_admin)
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

@user_passes_test(is_admin)
def admin_review_list(request):
    reviews = Review.objects.all()
    return render(request, 'admin_app/admin_review_list.html', {'reviews': reviews})

@user_passes_test(is_admin)
def admin_delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect(reverse('admin_review_list'))



def admin_registration(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            admin_group, created = Group.objects.get_or_create(name='Admin')
            user.groups.add(admin_group)
            return redirect('login')
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin_app/admin_registration.html', {'form': form})

from django.contrib import messages
from django.contrib.auth import logout

def admin_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')



def home(request):
    return render(request, 'admin_app/home.html')

def root_redirect(request):
    return redirect('login') 

from django.contrib.auth.views import LoginView


class GroupBasedLoginView(LoginView):
    template_name = 'admin_app/login.html' 

    def get_success_url(self):
        user = self.request.user
        if user.groups.filter(name='Admin').exists():
            return '/home/'
        elif user.groups.filter(name='User').exists():
            return '/home/'
        else:
            return '/'  

