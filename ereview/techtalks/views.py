
from django.shortcuts import render,get_object_or_404,redirect
from admin_app.models import Product, Review  
from .forms import ReviewForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required
def user_home(request):
    return render(request, 'techtalks/user_home.html')

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product  
            review.save()
            return redirect('product_detail', product_id=product.id)  
    else:
        form = ReviewForm()

    return render(request, 'techtalks/add_review.html', {'form': form, 'product': product})



@login_required
def browse_products(request):
    products = Product.objects.all()
    return render(request, 'techtalks/products.html', {'products': products})

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product).order_by('-created_at')
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()
        
    return render(request, 'techtalks/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form
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