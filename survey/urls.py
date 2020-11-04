from django.conf.urls import url

from . import views
app_name = 'survey'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote'),
    url('detail/', views.detail, name='detail'),
    url(r'^((?P<email>\[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}))/$',views.detail, name='detail'),
    url('needsurvey/', views.needSurvey, name='needsurvey'),
]
