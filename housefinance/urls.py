from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^chart_spend_data/$', views.chart_spend_data, name='chart_spend_data'),
    url(r'^chart_spend/$', views.ChartSpendView.as_view(), name='chart_spend')
]