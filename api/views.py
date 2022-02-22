<<<<<<< HEAD
<<<<<<< HEAD
from datetime import datetime

from django.shortcuts import render
=======
=======
>>>>>>> main

from .serializers import CMNSerializer, JSONSerializer
from .models import ArquivoJSON, CommonMercosulNomenclature
from rest_framework import generics 
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> main
import requests
from datetime import datetime

from django.shortcuts import render 

<<<<<<< HEAD

from api.models import CommonMercosulNomenclature

=======
>>>>>>> main

def index(request):
    response = requests.get('https://portalunico.siscomex.gov.br/classif/api/publico/nomenclatura/download/json')
    for item in response.json()['Nomenclaturas']:
<<<<<<< HEAD
<<<<<<< HEAD
        CommonMercosulNomenclature.objects.get_or_create(
            code=item['Codigo'],
            description=item["Descricao"],
            start_date=datetime.strptime(item["Data_Inicio"], '%d/%m/%Y'),
            finish_date=datetime.strptime(item["Data_Fim"], '%d/%m/%Y'),
            act_type=item["Tipo_Ato"],
            act_number=item["Numero_Ato"],
            act_year=item["Ano_Ato"],
        )
=======
=======
>>>>>>> main
       CommonMercosulNomenclature.objects.get_or_create(
            Codigo=item['Codigo'],
            Descricao=item["Descricao"],
            Data_Inicio=datetime.strptime(item["Data_Inicio"],'%d/%m/%Y'),
            Data_Fim=datetime.strptime(item["Data_Fim"],'%d/%m/%Y'),
            Tipo_Ato=item["Tipo_Ato"],
            Numero_Ato=item["Numero_Ato"],
            Ano_Ato=item["Ano_Ato"],
        )

    return render(request, 'index.html' )


class NomenclaturasList(generics.ListCreateAPIView):       
    queryset = CommonMercosulNomenclature.objects.all()
    serializer_class = CMNSerializer 
    
<<<<<<< HEAD
>>>>>>> main

class NomenclaturasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommonMercosulNomenclature.objects.all()
    serializer_class = CMNSerializer

    def get_object(self, pk):
        try:
            return CommonMercosulNomenclature.objects.get(pk=pk)
        except CommonMercosulNomenclature.DoesNotExist:
            raise #Http404

    def get(self, request, pk, format=None):
        detalhe = self.get_object(pk)
        serializer = CMNSerializer(detalhe)
        return #Response(serializer.data)

    def delete(self, request, pk, format=None):
        detalhe = self.get_object(pk)
        detalhe.delete()
        return #Response(status=status.HTTP_204_NO_CONTENT)
  

=======

class NomenclaturasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommonMercosulNomenclature.objects.all()
    serializer_class = CMNSerializer

    def get_object(self, pk):
        try:
            return CommonMercosulNomenclature.objects.get(pk=pk)
        except CommonMercosulNomenclature.DoesNotExist:
            raise #Http404

    def get(self, request, pk, format=None):
        detalhe = self.get_object(pk)
        serializer = CMNSerializer(detalhe)
        return #Response(serializer.data)

    def delete(self, request, pk, format=None):
        detalhe = self.get_object(pk)
        detalhe.delete()
        return #Response(status=status.HTTP_204_NO_CONTENT)
  

>>>>>>> main
class ArquivoList(generics.ListCreateAPIView):  
    queryset = ArquivoJSON.objects.all()
    serializer_class = JSONSerializer 
