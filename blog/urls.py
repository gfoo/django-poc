from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.accueil, name='accueil'),
    url(r'^article/(\d+)$', views.lire, name='lire'),
    # url(r'^article/(\d+)$', views.view_article),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_articles),
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition)
]
