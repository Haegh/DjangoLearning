from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime
from .models import Article, Contact
from .forms import ContactForm, NouveauContactForm


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


def accueil(request):
    """ Afficher tous les articles """
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})


def lire(request, id, slug):
    """ Afficher un article complet """
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article': article})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']
        envoi = True

    return render(request, 'blog/contact.html', locals())


def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'blog/contact2.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })
