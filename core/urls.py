from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from core import views

schema_view = get_swagger_view(title='EdificioWebAPI')

urlpatterns = [
    url(r'^user/$',
        views.UserList.as_view(),
        name=views.UserList.name),
    url(r'^user/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name=views.UserDetail.name),
    url(r'^cliente/$',
        views.ClienteList.as_view(),
        name=views.ClienteList.name),
    url(r'^cliente/(?P<pk>[0-9]+)/$',
        views.ClienteDetail.as_view(),
        name=views.ClienteDetail.name),
    url(r'^sala/$',
        views.SalaList.as_view(),
        name=views.SalaList.name),
    url(r'^sala/(?P<pk>[0-9]+)/$',
        views.SalaDetail.as_view(),
        name=views.SalaDetail.name),
    url(r'^profissional/$',
        views.ProfissionalList.as_view(),
        name=views.ProfissionalList.name),
    url(r'^profissional/(?P<pk>[0-9]+)/$',
        views.ProfissionalDetail.as_view(),
        name=views.ProfissionalDetail.name),
    url(r'^escritorio/$',
        views.EscritorioList.as_view(),
        name=views.EscritorioList.name),
    url(r'^escritorio/(?P<pk>[0-9]+)/$',
        views.EscritorioDetail.as_view(),
        name=views.EscritorioDetail.name),
    url(r'^agenda/$',
        views.ItemAgendaList.as_view(),
        name=views.ItemAgendaList.name),
    url(r'^agenda/(?P<pk>[0-9]+)/$',
        views.ItemAgendaDetail.as_view(),
        name=views.ItemAgendaDetail.name),
    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
    url(r'^swagger/$', schema_view),
    ]