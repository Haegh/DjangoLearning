from django.urls import path, re_path
from . import views


urlpatterns = [
    #path('accueil', views.home),
    #path('article/<int:id_article>', views.view_article, name='afficher_article'),
    #re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.list_articles),
    #path('redirection', views.view_redirection),
    #path('date', views.date_actuelle),
    #path('addition/<int:nombre1>/<int:nombre2>', views.addition),
    path('', views.accueil, name='accueil'),
    path('articles/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('contact/', views.contact, name='contact'),
    path('contact2/', views.nouveau_contact, name='nouveau_contact'),
]
