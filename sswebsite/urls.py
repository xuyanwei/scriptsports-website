from django.conf.urls import include, url
from scriptsports import views
from django.contrib import admin,auth
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'sswebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.mainecho),
    url(r'^live_kankan/$',views.livekanecho),
    url(r'^video_list/$',views.videolistecho),


    url(r'^jijin/$',views.jijinecho),
    url(r'^stream/$',views.streamecho),
    url(r'^stream_extr/$',views.streamextrecho),
    url(r'^video/$',views.videoecho),


    url(r'^news_deta/$',views.newsecho),
    url(r'^news/$',views.newslistecho),

    url(r'^newsch/$',views.newschecho),
    url(r'^showch/$',views.showchecho),

    url(r'^live/$',views.liveecho),
    url(r'^data/$',views.dataecho),

    url(r'^about/$',views.aboutecho),

    url(r'^loginin/$',views.register),
    url(r'^login/$',views.login),
    url(r'^loginout/$',views.loginout),
    url(r'^changeps/$',views.changeps),

    url(r'^bbs/$',views.bbs),
    url(r'^bbs_talk/$',views.bbstalk),
    url(r'^sharing/$',views.sharing),
    url(r'^ttalk/$',views.ttalk),

    url(r'^admin/', include(admin.site.urls)),
]
