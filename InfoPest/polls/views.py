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

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
                'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))