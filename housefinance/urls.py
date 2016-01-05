from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^accounting_document/$', views.AccountingDocumentIndexView.as_view(), name='acc_doc_index'),
    url(r'^accounting_document/(?P<pk>[0-9]+)/$', views.AccountingDocumentDetailView.as_view(), name='acc_doc_detail'),
    url(r'^accounting_document/add/$', views.AccountingDocumentCreateView.as_view(), name='acc_doc_add'),
    url(r'^chart_spend/$', views.chart_spend, name='chart_spend'),
    url(r'^fibonacci/(?P<m>[0-9]+)$', views.fibonacci, name='fibonacci')
]