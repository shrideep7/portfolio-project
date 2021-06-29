from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=200 , default = '')

	body = models.TextField(max_length=200,default='')
	image = models.ImageField(upload_to='image/')

	def summary(self):
		return self.body[:20]



	def __str__(self):
		return self.title