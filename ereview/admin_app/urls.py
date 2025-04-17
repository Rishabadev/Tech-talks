from django.urls import path
from .views import add_product,edit_product,delete_product,admin_product_list,admin_dashboard,admin_review_list,admin_delete_review
from .views import admin_registration, admin_logout,home

from .views import admin_registration, GroupBasedLoginView

urlpatterns = [
    
    path('home/',home, name='home'),
   
    
    path('admin_dashboard/',admin_dashboard, name = 'admin_dashboard'),
    
    
    path('admin-products/',admin_product_list, name='admin_product_list'),
    path('add-product/',add_product,name='add_product'),
    path('edit-product/<int:product_id>/',edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/',delete_product, name='delete_product'),
    

    path('reviews/', admin_review_list, name='admin_review_list'),
    path('review/delete/<int:review_id>/', admin_delete_review, name='admin_delete_review'),
    
 


    path('admin-registration/', admin_registration, name='admin_registration'),

    path('login/', GroupBasedLoginView.as_view(), name='login'),
    path('logout/', admin_logout, name='admin_logout'),



]