from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render


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
