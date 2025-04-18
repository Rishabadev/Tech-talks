from django.urls import path 
from . import views


urlpatterns = [
    path('', views.user_home, name='user_home'),

    path('products/', views.browse_products, name='browse_products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/<int:product_id>/add-review/', views.add_or_edit_review, name='add_review'),

    path('my-reviews/', views.my_reviews, name='my_reviews'),

    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    path('register/', views.user_registration, name='user_registration'),
]
