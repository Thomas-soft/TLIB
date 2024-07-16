from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    a = models.ImageField(upload_to="images/", blank=True, null=True)
    pass
    # Les champs username, email, password, etc., sont déjà inclus dans AbstractUser