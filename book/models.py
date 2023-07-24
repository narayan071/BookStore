from django.db import models
from django.contrib.auth.models import User
from user.models import Address

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "Categories"
    
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="book_images", null=True, blank=True)

    def __str__(self):
        return self.title
    

class Order(models.Model):
    STATUS_OPTION = [
        ('placed', 'placed'),
        ('packed', 'packed'),
        ('shipped', 'shipped'),
        ('delivered', 'delivered'),
        ('cancelled', 'cancelled'),
    ]

    PAYMENT_MODES = [
        ('COD', 'COD'),
        ('Online', 'Online'),
    ]

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    price = models.FloatField()
    status = models.CharField(max_length=20, choices = STATUS_OPTION, default='placed')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_MODES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name+" "+self.book.title

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    book =models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.book.title+" - "+self.comment
    


