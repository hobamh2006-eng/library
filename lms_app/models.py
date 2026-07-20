from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Books(models.Model):

    status_choices = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('sold', 'Sold'),
    ]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50,null=True, blank=True)
    book_photo = models.ImageField(upload_to='photos', null=True, blank=True)
    author_photo = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True , blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rental_price_per_day = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    total_rental = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rental_period = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=status_choices ,null=True, blank=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

     
    def __str__(self):
        return f"{self.title} => {self.author}...........(({self.category}))"