from django.db import models
from django.contrib.auth.models import User

# Perfil del Usuario
class Profile(models.Model):
	user = models.ForeignKey(User)


	def __unicode__(self):
		return self.user.username + ' Profile'