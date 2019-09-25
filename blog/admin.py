from django.contrib import admin
from django.utils.text import  Truncator
from .models import Categorie, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date')
    list_filter = ('auteur', 'categorie',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre',), }

    def apercu_contenu(self, article):
        """ Retourne les 40 premiers char """
        return Truncator(article.contenu).chars(40, truncate='...')

    apercu_contenu.short_description = 'Apercçu du contenu'


admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
