import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','newtrade.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random
from affiliate.models import Homedecor
import pandas as pd

#Name of file to be imported
loc = ("homedecor.xlsx")
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
            flag =  Homedecor.objects.get(prod_title=prodTitle)
            Homedecor.objects.filter(prod_title=prodTitle).update(Price=price)
        except Homedecor.DoesNotExist:
            homedecor = Homedecor.objects.create(Image=image,prod_title=prodTitle,Price=price,Url=url)

if __name__ == '__main__':
    print("Reading homedecor_excel")
    populate()
    print("populating homedecor complete")
