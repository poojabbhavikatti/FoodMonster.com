from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional fields
    ID_proof = models.ImageField(blank=True)
    
    user_url = models.URLField(blank=True)


