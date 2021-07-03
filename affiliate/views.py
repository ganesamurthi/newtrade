from django.shortcuts import render
from itertools import chain
from affiliate.models import Cookware, Crockery, Furniture, Clothing, Homedecor

from django.core.paginator import Paginator

# product lists
crockery_list = Crockery.objects.order_by('-created_time')
cookware_list = Cookware.objects.order_by('-created_time')
furniture_list = Furniture.objects.order_by('-created_time')
clothing_list = Clothing.objects.order_by('-created_time')
homedecor_list = Homedecor.objects.order_by('-created_time')

index_list = list(chain(cookware_list[:5],crockery_list[:5],homedecor_list[:5],clothing_list[:5],furniture_list[:5]))


# cookware_index = Cookware.objects.order_by('-created_time')[:5]
# crockery_index = Crockery.objects.order_by('-created_time')[:5]
# furniture_index = Furniture.objects.order_by('-created_time')[:5]
# clothing_index = Clothing.objects.order_by('-created_time')[:5]
# homedecor_index = Homedecor.objects.order_by('-created_time')[:5]
# Create your views here.
def index(request):
    indexdict = {'indexlist' : index_list}
    return render(request,'affiliate/index.html',context=indexdict)

def crockery(request):
    # set up Pagination
    p = Paginator(crockery_list,10)
    page = request.GET.get('page')
    crockerys = p.get_page(page)
    crockerydict = {'crockerys':crockerys}
    return(render(request,'affiliate/crockery.html', context=crockerydict))

def furniture(request):
    # set up Pagination
    p = Paginator(furniture_list,1)
    page = request.GET.get('page')
    furnitures = p.get_page(page)
    furnituredict = {'furnitures':furnitures}
    return(render(request,'affiliate/furniture.html', context=furnituredict))

def clothing(request):
    # set up Pagination
    p = Paginator(clothing_list,1)
    page = request.GET.get('page')
    clothings = p.get_page(page)
    clothingdict = {'clothings':clothings}
    return(render(request,'affiliate/clothing.html', context=clothingdict))

def homedecor(request):
    # set up Pagination
    p = Paginator(homedecor_list,10)
    page = request.GET.get('page')
    homedecors = p.get_page(page)
    homedecordict = {'homedecors':homedecors}
    return(render(request,'affiliate/homedecor.html', context=homedecordict))

def cookware(request):
    # set up Pagination
    p = Paginator(cookware_list,10)
    page = request.GET.get('page')
    cookwares = p.get_page(page)
    cookwaredict = { 'cookwares':cookwares}
    return(render(request, 'affiliate/cookware.html', context=cookwaredict))
