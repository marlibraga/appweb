
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_list(request):
    return render(request, 'appweb/post_list.html')
    

def sobre(request):
    return render(request, 'appweb/sobre.html')


def contato(request):
    return render(request, 'appweb/contato.html')
