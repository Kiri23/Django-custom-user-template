from django.shortcuts import render

# Create your views here.


def inscribete(request):
    return render(request, "inscribete/inscribete.html")
