from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'brodus.views.index', name='index'),
                       url(r'^user/log_in$','brodus.views.log_in', name='log_in'),
                       url(r'^user/new$','brodus.views.new_user', name='new_user'),
                       url(r'^user/log_out$','brodus.views.log_out', name='log_out'),
                       url(r'^add/new$','brodus.views.add_new', name='add_new'),
                       url(r'^new/proyecto$','brodus.views.new_proy', name='new_proy'),
                       url(r'^mod/proyecto/(?P<proj>[0-9]+)$','brodus.views.mod_proy', name='mod_proy'),
                       url(r'^del/proyecto/(?P<proj>[0-9]+)$','brodus.views.del_proy', name='del_proy'),
                       url(r'^add/work/(?P<w_p>[0-9]+)$','brodus.views.n_p_w', name='add_work'),
                       url(r'^del/work/(?P<w_p>[0-9]+)$','brodus.views.d_p_w', name='del_work'),
                       url(r'^create/proj$','brodus.views.n_p', name='create_proj'),
                      )
