import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','indtrade.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random
from affiliate.models import Homedecor,Cookware,Crockery,Clothing,Furniture

# delete all rows
Homedecor.objects.all().delete()
Clothing.objects.all().delete()
Cookware.objects.all().delete()
Crockery.objects.all().delete()
Furniture.objects.all().delete()
