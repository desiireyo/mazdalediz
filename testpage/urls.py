from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    # index_search,
    # index_order,
    
    index_new,
    save_prospect,
    load_resourcemore,
    index_view,
    prospect_delete,
    prospect_edit,
    prospect_update,
    index_searchstock,
    prospect_login,
)

urlpatterns = [
    # url(r'^$',index_search,name='index_search'),
    # url(r'^order',index_order,name='index_order'),
    # url(r'^print',index_print,name='index_print'),

    # url(r'^ins_settype',ins_settype,name='ins_settype'),

    url(r'^stock$',index_searchstock,name='index_searchstock'),
    url(r'^$',prospect_login,name='secret'),

    url(r'^new',index_new,name='index_new'),
    url(r'^save_prospect',save_prospect,name='save_prospect'),
    url(r'^index_view',index_view,name='index_view'),

    url(r'^prospect_delete/(?P<id>\d+)$', prospect_delete, name='prospect_delete'),
    url(r'^prospect_edit/(?P<id>\d+)$', prospect_edit, name='prospect_edit'),
    url(r'^prospect_update/(?P<id>\d+)$', prospect_update, name='prospect_update'),

    url(r'^ajaxload_resource', load_resourcemore, name='ajax_load_resourcemore'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)