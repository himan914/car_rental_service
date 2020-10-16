from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.FileField(upload_to='products/%Y/%m/%d',blank=True)

    price = models.DecimalField(max_digits=10,decimal_places=2)

    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    seats=models.IntegerField(null=True)
    milege=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    


    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])



class Booking(models.Model):
    car = models.ForeignKey(Product,null=True)

    cname = models.CharField(max_length=100)
    email = models.EmailField()
    ph_no = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    Address = models.TextField()

    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return self.cname



'''class Detail(models.Model):
    car=models.ForeignKey(Car)
    carname=models.CharField(max_length=20)
    seats=models.IntegerField()
    Frontac = models.BooleanField()
    backac = models.BooleanField()
    color=models.CharField(max_length=10)
    milege=models.IntegerField()
    model=models.IntegerField()

    def __str__(self):
        return self.carname'''
