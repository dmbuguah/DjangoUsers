import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	"""docstring for ClassName"""
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField()

	def __unicode__(self):
		return self.title
	

