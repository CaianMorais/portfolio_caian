from django.http import JsonResponse
from django.shortcuts import render
from portfolio_admin.models import Projetos, Sobre, Tecnologias, Curriculo

# Create your views here.

def index(request):
    projetos = Projetos.objects.filter(publico=True).order_by("-id")
    sobre = Sobre.objects.filter(publico=True).first()
    tecnologias = Tecnologias.objects.filter(publico=True).order_by("-id")
    curriculo = Curriculo.objects.filter(publico=True).first()

    return render(request, "projetos/index.html", {
        "projetos": projetos,
        "sobre": sobre,
        "tecnologias": tecnologias,
        "curriculo": curriculo,
    })

def localizar_curriculo(request):
    curriculo = Curriculo.objects.filter(publico=True).first()
    path = curriculo.arquivo.url
    return JsonResponse({"path": path}, safe=False)