from django.conf.urls import url 
from . import views

urlpatterns = [ 
    url(r'^$', views.show_questions, name='questions'),
    url(r'^getresult/$', views.get_result, name='get_result'),
    url(r'^analyze/$', views.analyze, name='analyze'),
    url(r'^testredis/$', views.test_redis, name='test_redis'),
]