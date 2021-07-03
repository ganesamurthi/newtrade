from django.urls import path
from affiliate import views

#TEMAPLATE TAGGIG
app_name = 'affiliate'

urlpatterns = [
    path('',views.index, name='index'),
    path('cookware/',views.cookware, name='cookware'),
    path('crockery/',views.crockery, name='crockery'),
    path('furniture/',views.furniture, name='furniture'),
    path('clothing/',views.clothing, name='clothing'),
    path('homedecor/',views.homedecor, name='homedecor'),

]
