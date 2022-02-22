from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns 


urlpatterns = [
    path('', views.ArquivoList.as_view(), name='view-arquivo'),
    path('lista/', views.NomenclaturasList.as_view(), name='view-ncms'), 

    path('test', views.index, name='view'),

]

urlpatterns = format_suffix_patterns(urlpatterns)