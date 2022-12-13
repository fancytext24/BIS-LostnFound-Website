from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    # many to one relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ("EL", "Electronics"),
    ("SH", "Shirts"),
    ("PS", "Pants/Shorts"),
    ("FW", "Footware"),
    ("ST", "Stationaries"),
    ("BG", "Bags"),
    ("SG", "Scarfs, hats and gloves"),
    ("LB", "Lunch Boxes"),
    ("WB", "Water Bottles"),
    ("VB", "Valuables"),
    ("OT", "Others"),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to="productimg")

    def __str__(self):
        return str(self.id)


class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return 0


STATUS_CHOICES = (
    ("Accepted", "Accepted"),
    ("Delivered", "Delivered"),
    ("Cancel", "Cancel"),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default="Pending")

    @property
    def total_cost(self):
        return 0
