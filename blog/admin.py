from django.contrib import admin
from .models import Categorie, Article
from django.utils.text import Truncator

admin.site.register(Categorie)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur', 'categorie',)
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('titre', 'contenu')

    def apercu_contenu(self, article):
        return Truncator(article.contenu).chars(40, truncate='...')

    apercu_contenu.short_description = 'Apercu du contenu'


admin.site.register(Article, ArticleAdmin)
