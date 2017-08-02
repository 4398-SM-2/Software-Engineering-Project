from django.db import models

class images(models.Model):
	filename = models.TextField()
	
	def __str__ (self):
		return self.filename