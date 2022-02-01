from django.shortcuts import render
import requests

def index(request):
    #if request.method == 'POST':
    downloadURL = requests.get('https://portalunico.siscomex.gov.br/classif/api/publico/nomenclatura/download/json')
    
    print(downloadURL.json())
    print(downloadURL.status_code)
    
    #cpf = request.POST.get(['cpf'])

    return render(request, 'index.html')
