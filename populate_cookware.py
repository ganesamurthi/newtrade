import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','newtrade.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random
from affiliate.models import Cookware
import pandas as pd

#Name of file to be imported
loc = ("cookware.xlsx")
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
            flag =  Cookware.objects.get(prod_title=prodTitle)
            Cookware.objects.filter(prod_title=prodTitle).update(Price=price)
        except Cookware.DoesNotExist:
            cookware = Cookware.objects.create(Image=image,prod_title=prodTitle,Price=price,Url=url)

if __name__ == '__main__':
    print("Reading cookware_excel")
    populate()
    print("populating cookware complete")
