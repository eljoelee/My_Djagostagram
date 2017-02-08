from django.conf.urls import url
from . import  views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^photos/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^photos/upload/$', views.create, name='create'),
]
urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)