from django.shortcuts import render
from portfolio_admin.models import Projetos, Sobre, Tecnologias, Contato, Curriculo

# Create your views here.

def index(request):
    projetos = Projetos.objects.filter(publico=True)
    sobre = Sobre.objects.filter(publico=True).first()
    tecnologias = Tecnologias.objects.filter(publico=True)
    contatos = Contato.objects.all()
    curriculo = Curriculo.objects.filter(publico=True).first()

    return render(request, "projetos/index.html", {
        "projetos": projetos,
        "sobre": sobre,
        "tecnologias": tecnologias,
        "contatos": contatos,
        "curriculo": curriculo,
    })