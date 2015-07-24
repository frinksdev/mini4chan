from django.db import models
from django.utils import timezone

class chan(models.Model):
	autor=models.ForeignKey("auth.User", blank=True, null=True)
	titulo=models.CharField(max_length=200)
	contenido=models.TextField()
	c_date=models.DateTimeField(default=timezone.now)
	p_date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.titulo

class comentario(models.Model):
	post=models.ForeignKey(chan)
	comentario=models.CharField(max_length=400)
	p_date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.comentario