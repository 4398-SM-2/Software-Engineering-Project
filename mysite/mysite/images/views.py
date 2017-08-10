from django.shortcuts import render

def images(request):
	return render (request, 'images/images.html')