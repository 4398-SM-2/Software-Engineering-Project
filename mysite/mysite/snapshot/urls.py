from django.conf.urls import url, include
from images.models import images


urlpatterns = [
	url(r'^$', veiws.snapshot , name = 'snapshot')
]
