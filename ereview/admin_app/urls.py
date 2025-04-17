from django.urls import path
from .views import add_product,edit_product,delete_product,admin_product_list,admin_dashboard,admin_review_list,admin_delete_review
from .views import admin_registration, admin_logout,home

from .views import admin_registration, GroupBasedLoginView

from django.contrib.auth import views as auth_views
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

    

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='admin_app/pass_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='admin_app/pass_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='admin_app/pass_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='admin_app/pass_reset_complete.html'), name='password_reset_complete'),

]