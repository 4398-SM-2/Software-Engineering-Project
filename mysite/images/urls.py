from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from images.models import images


urlpatterns = [
	url(r'^$', ListView.as_view(queryset=images.objects.all().order_by("-filename")[:25], 
	template_name='images/images.html'), name = 'images')
]
