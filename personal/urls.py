from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^projects', views.projects, name='projects'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^posts/(?P<post_id>.*)/$', views.blog_posts, name='posts'),
    url(r'^demo/(?P<proj_id>.*)/$', views.proj, name='demo'),
]
