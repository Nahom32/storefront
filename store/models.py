from django.db import models
#from .models import Collection, Customer, Order,Cart

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey('Collection', on_delete=models.PROTECT)
    promotion = models.ManyToManyField(Promotion)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)
    # class Meta:
    #     db_table = 'store_customers'
    #     indexes = [
    #         models.Index(fields=['last_name','first_name'])
    #     ]
    
    class Order(models.Model):
        PAYMENT_PENDING = 'P'
        PAYMENT_COMPLETE = 'C'
        PAYMENT_FAILED = 'F'
        PAYMENT_FIELDS = [
            (PAYMENT_PENDING,'Pending'),
            (PAYMENT_COMPLETE,'Complete'),
            (PAYMENT_FAILED,'Failed')
        ]
        placed_at = models.DateTimeField(auto_now_add=True)
        payment_status = models.CharField(max_length=1, choices=PAYMENT_FIELDS, default=PAYMENT_PENDING)
    class Address(models.Model):
        street = models.CharField(max_length=255)
        city = models.CharField(max_length=255)
        customer= models.ForeignKey('Customer',on_delete=models.CASCADE)
        zip = models.CharField(max_length=255, null=True)
    class Collection(models.Model):
        title = models.CharField(max_length=255)
    class OrderItem(models.Model):
        order= models.ForeignKey('Order',on_delete=models.PROTECT)
        product = models.ForeignKey(Product,on_delete=models.PROTECT)
        quantity = models.PositiveSmallIntegerField()
        unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    class Cart(models.Model):
        created_at = models.DateTimeField(auto_now_add=True)
    class CartItem(models.Model):
        cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.PositiveSmallIntegerField()
        
        
        
        