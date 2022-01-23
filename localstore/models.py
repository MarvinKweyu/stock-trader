from django.db import models

# Create your models here.


class Product(models.Model):
    """A single item in the store"""
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # description = models.TextField()
    # quantity of this product
    inventory = models.IntegerField(default=20)
    re_order_level = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class Reorder(models.Model):
    """A reorder item"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    CHOICES = (
        ('Proc', 'Processed'),
        ('Pend', 'Pending'),
    )
    status = models.CharField(max_length=4, choices=CHOICES, default='Pend')
    reorder_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name
