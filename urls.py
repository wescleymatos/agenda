from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gerenciador.views.home', name='home'),
    # url(r'^gerenciador/', include('gerenciador.foo.urls')),
    url(r'^$', 'agenda.views.index'),
    url(r'^lista/$', 'agenda.views.lista'),
    url(r'^adiciona/$', 'agenda.views.adiciona'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

