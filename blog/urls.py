from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^article/(\d+)$', views.view_article),  # Vue d'un article
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_articles),
]
