from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib import messages
from flans.models import Flan,FlanPage,FormContact

def index(request):
    flanPage = FlanPage.objects.all()
    flans = Flan.objects.all()
    context ={
        'flanPage':flanPage,
        'flans':flans
    }
    return render(request, 'index.html', context)

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        formContact = FormContact(name=name, email=email, message=message)
        formContact.save()
        messages.success(request, 'Formulario enviado exitosamente')
        return redirect('index')
    return redirect('index')
