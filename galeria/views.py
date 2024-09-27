from django.shortcuts import render



def index(request):
    dados = {
    1:{"nome":"Lucas corredor",
       "legenda":"A corrida salva vidas!"},
    2:{"nome":"Lucas atleta",
       "legenda":"Sem pressa e sem pausa"}
    }
    return render(request, 'galeria/index.html',{"cards":dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')



