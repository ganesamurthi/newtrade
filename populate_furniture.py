import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','newtrade.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random
from affiliate.models import Furniture
import pandas as pd

#Name of file to be imported
loc = ("furniture.xlsx")
df = pd.read_excel(loc)

# for row in df.itertuples():
#     print(row.Price)

def populate():

    for row in df.itertuples():
        image = row.ImageTextUrl
        prodTitle = row.ProdTitle
        price = row.Price
        url = row.TxtUrl

        try:
            flag =  Furniture.objects.get(prod_title=prodTitle)
            Furniture.objects.filter(prod_title=prodTitle).update(Price=price)
        except Furniture.DoesNotExist:
            furniture = Furniture.objects.create(Image=image,prod_title=prodTitle,Price=price,Url=url)

if __name__ == '__main__':
    print("Reading furniture_excel")
    populate()
    print("populating furniture complete")
