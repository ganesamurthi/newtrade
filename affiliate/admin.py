from django.contrib import admin
from affiliate.models import Cookware, Crockery, Furniture, Clothing, Homedecor

# Register your models here.
admin.site.register(Cookware)
admin.site.register(Crockery)
admin.site.register(Furniture)
admin.site.register(Clothing)
admin.site.register(Homedecor)
