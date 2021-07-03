import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','newtrade.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random
from affiliate.models import Crockery
import pandas as pd

#Name of file to be imported
loc = ("crockery.xlsx")
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
            flag =  Crockery.objects.get(prod_title=prodTitle)
            Crockery.objects.filter(prod_title=prodTitle).update(Price=price)
        except Crockery.DoesNotExist:
            crockery = Crockery.objects.create(Image=image,prod_title=prodTitle,Price=price,Url=url)



if __name__ == '__main__':
    print("Reading crockery_excel")
    populate()
    print("populating crockery complete")
