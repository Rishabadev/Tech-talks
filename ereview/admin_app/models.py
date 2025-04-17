from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100,unique =True)

    def __str__(self):
        return self.name


class Product(models.Model):
    
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = "products")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_images/")
    

    def __str__(self):
        return self.name
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)])
    comment = models.TextField()
    image = models.ImageField(upload_to="review_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.rating})"
    
