from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from datetime import datetime


def home(request):
    """ Exemple de page non valide """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes c'est trop bon !</p>
    """)


def view_article(request, id_article):
    """
    Vue qui affiche un article selon son ID
    Son ID est le second param
    """
    # Si l'ID est supérieure à 100, on considére qu'il n'existe pas
    if id_article > 100:
        raise Http404

    return redirect('afficher_article', id_article=42)
    #return HttpResponse(
    #    "Vous avez demandé l'article n°{0} !".format(id_article)
    #)


def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """

    return HttpResponse(
        "Vous avez demandé les articles de {0} {1}".format(month, year)
    )


def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    return render(request, 'blog/addition.html', locals())
