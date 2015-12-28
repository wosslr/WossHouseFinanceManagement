from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^chart_spend/$', views.chart_spend, name='chart_spend'),
    url(r'^fibonacci/(?P<m>[0-9]+)$', views.fibonacci, name='fibonacci')
]