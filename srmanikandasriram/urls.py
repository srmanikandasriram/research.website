from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', TemplateView.as_view(template_name="index.html")),
	(r'^index/', TemplateView.as_view(template_name="index.html")),
	(r'^education/', TemplateView.as_view(template_name="education.html")),
	(r'^research/', TemplateView.as_view(template_name="research.html")),
	(r'^resume/', TemplateView.as_view(template_name="resume.html")),
	(r'^webops/', TemplateView.as_view(template_name="webops.html")),
	(r'^contact/', TemplateView.as_view(template_name="contact.html")),
    # Examples:
    # url(r'^$', 'srmanikandasriram.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
