from django.db import models

class Cookware(models.Model):
    Image = models.CharField(max_length=1024)
    prod_title = models.CharField(max_length=1024)
    Price = models.DecimalField(max_digits=11,decimal_places=2)
    Url = models.CharField(max_length=254)
    created_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.prod_title

class Crockery(models.Model):
    Image = models.CharField(max_length=1024)
    prod_title = models.CharField(max_length=1024)
    Price = models.DecimalField(max_digits=11,decimal_places=2)
    Url = models.CharField(max_length=254)
    created_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.prod_title

class Clothing(models.Model):
    Image = models.CharField(max_length=1024)
    prod_title = models.CharField(max_length=1024)
    Price = models.DecimalField(max_digits=11,decimal_places=2)
    Url = models.CharField(max_length=254)
    created_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.prod_title

class Furniture(models.Model):
    Image = models.CharField(max_length=1024)
    prod_title = models.CharField(max_length=1024)
    Price = models.DecimalField(max_digits=11,decimal_places=2)
    Url = models.CharField(max_length=254)
    created_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.prod_title

class Homedecor(models.Model):
    Image = models.CharField(max_length=1024)
    prod_title = models.CharField(max_length=1024)
    Price = models.DecimalField(max_digits=11,decimal_places=2)
    Url = models.CharField(max_length=254)
    created_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.prod_title

# Create your models here.
