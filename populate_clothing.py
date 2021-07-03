import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','newtrade.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random
from affiliate.models import Clothing
import pandas as pd

#Name of file to be imported
loc = ("clothing.xlsx")
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
            flag =  Clothing.objects.get(prod_title=prodTitle)
            Clothing.objects.filter(prod_title=prodTitle).update(Price=price)
        except Clothing.DoesNotExist:
            clothing = Clothing.objects.create(Image=image,prod_title=prodTitle,Price=price,Url=url)


if __name__ == '__main__':
    print("Reading Clothing_excel")
    populate()
    print("populating clothing complete")
