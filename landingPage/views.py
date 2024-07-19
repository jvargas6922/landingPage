from django.shortcuts import render
from django.http import HttpResponse
from flans.models import Flan,FlanPage,FormContact

def index(request):
    flanPage = FlanPage.objects.all()
    flans = Flan.objects.all()
    context ={
        'flanPage':flanPage,
        'flans':flans
    }
    return render(request, 'index.html', context)

def form(requets):
    if requets.method == 'POST':
        name = requets.POST.get('name')
        email = requets.POST.get('email')
        message = requets.POST.get('message')
        formContact = FormContact(name=name,email=email,message=message)
        formContact.save()
        return HttpResponse('Formulario enviado exitosamente')
