from django.shortcuts import render

# Create your views here.


def matricula(request):
    return render(request, "matricula/matricula.html")
