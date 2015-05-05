from django.conf.urls import patterns, url

urlpatterns = patterns('webapp.views',
	url(r'^$','index'),
	url(r'^addpurchase/$','addpurchase'),
	url(r'^get-users-by-name/$','getUsersByName'),
	url(r'^get-purchase-users/$','getPurchaseUsers'),
	url(r'^ldap-sync/$','ldapSync')
)

urlpatterns += patterns('webapp.api.depart_controller',
    url(r'^departs/$', 'departs')
)

urlpatterns += patterns('webapp.api.user_controller',
    url(r'^get-users/$', 'getUsers')
)