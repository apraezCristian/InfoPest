from django.urls import path
from . import views
#usuarios.objects.filter(usuario__startswith='yulian')
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('lol/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('registro/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('vote/', views.vote, name='vote'),
]
