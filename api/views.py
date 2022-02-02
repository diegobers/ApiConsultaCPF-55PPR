from datetime import datetime

from django.shortcuts import render
import requests

from api.models import CommonMercosulNomenclature


def index(request):
    response = requests.get('https://portalunico.siscomex.gov.br/classif/api/publico/nomenclatura/download/json')
    for item in response.json()['Nomenclaturas']:
       CommonMercosulNomenclature.objects.get_or_create(
            code=item['Codigo'],
            description=item["Descricao"],
            start_date=datetime.strptime(item["Data_Inicio"],'%d/%m/%Y'),
            finish_date=datetime.strptime(item["Data_Fim"],'%d/%m/%Y'),
            act_type=item["Tipo_Ato"],
            act_number=item["Numero_Ato"],
            act_year=item["Ano_Ato"],
        )

    return render(request, 'index.html')
