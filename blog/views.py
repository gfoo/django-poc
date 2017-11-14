from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render
from datetime import datetime

from blog.models import Article


def accueil(request):
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})


def lire(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'blog/lire.html', {'article': article})


def home(request):
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crepes bretonnes ca tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)


def view_article(request, id_article):
    if int(id_article) > 100:
        raise Http404
    return HttpResponse(
        "Vous avez demande l'article #{0} !".format(id_article)
    )


def list_articles(request, month, year):
    return HttpResponse(
        "Vous avez demande les articles de {0} {1}.".format(month, year)
    )


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())
