
from django.shortcuts import render,get_object_or_404,redirect
from admin_app.models import Product,Review

from .forms import ReviewForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required
def user_home(request):
    return render(request, 'techtalks/user_home.html')

@login_required
def add_or_edit_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        review = Review.objects.get(product=product, user=request.user)
    except Review.DoesNotExist:
        review = None

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product = product
            new_review.user = request.user
            new_review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'techtalks/review.html', {'form': form, 'product': product})



@login_required
def browse_products(request):
    products = Product.objects.all()
    return render(request, 'techtalks/products.html', {'products': products})

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product).order_by('-created_at')
    try:
        user_review = Review.objects.get(product=product, user=request.user)
    except Review.DoesNotExist:
        user_review = None

    return render(request, 'techtalks/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'user_review': user_review
    })

@login_required
def my_reviews(request):
    reviews = Review.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'techtalks/my_reviews.html', {'reviews': reviews})

@login_required
def profile_view(request):
    return render(request, 'techtalks/profile.html', {'user': request.user})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'techtalks/edit_profile.html', {'form': form})

def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'techtalks/register.html', {'form': form})