 
from rest_framework import serializers, fields
from .models import CommonMercosulNomenclature, ArquivoJSON 


class CMNSerializer(serializers.ListSerializer):    

    class Meta:
        model = CommonMercosulNomenclature
        fields = '__all__'
    

class JSONSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model = ArquivoJSON 
        list_serializer_class = CMNSerializer
        fields = ['Data_Ultima_Atualizacao_NCM']
 
    