from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, usuarios
from django.urls import reverse
from django.http import Http404
from django.template import loader
# return render(request, 'polls/index.html', context)

def index(request):
    return render(request, 'polls/index.html')

def detail(request):
    context = {}
    usuario = request.POST.get('uname')
    contrasena = request.POST.get('psw')
    usuario_query = usuarios.objects.filter(usuario=usuario)
    contrasena_query = usuarios.objects.filter(contrasena=contrasena)
    if not usuario_query and not usuario_query:
        context['uname'] = 'no'
        context['psw'] = 'no'
    else:
        context['uname'] = usuario
        context['psw'] = contrasena
    return render(request, 'polls/detail.html',context)

def results(request):
    return render(request, 'polls/results.html')

def vote(request):
    email = request.POST.get('email')
    usuarioxd = request.POST.get('uname')
    password = request.POST.get('psw')
    psw_repeat = request.POST.get('psw-repeat')
    edadd = request.POST.get('edad')
    sexoo = 'nose'
    nuevo_usuario = usuarios(usuario=usuarioxd, contrasena=password, email_user=email, sexo=sexoo, edad=edadd)
    nuevo_usuario.save()
    context = {}
    context['uname'] = usuarioxd
    return render(request, 'polls/detail.html', context)