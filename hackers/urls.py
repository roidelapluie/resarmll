from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from hackers.views import HackerUpdate
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
        (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'resarmll/login_form.html'}),
        (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'resarmll/logout.html'}),
        url(r'^profile/$', login_required(TemplateView.as_view(template_name="resarmll/profile.html")), name='hackers_profile'),
        url(r'^profile/edit$', HackerUpdate.as_view(template_name="resarmll/profile_edit.html", success_url='/accounts/profile/'), name='hackers_update'),
    )

