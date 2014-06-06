from django.conf import settings

def static_url(request):
	return {'static_url': settings.STATIC_URL}

def site_url(request):
	return {'site_url': settings.SITE_URL}
