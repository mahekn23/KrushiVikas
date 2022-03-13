from email.policy import default
from django.db import models
from django.db.models import Model
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class RentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    uid = models.AutoField(primary_key=True)
    tool_name = models.CharField(max_length=500, blank=True)
    owner_name = models.CharField(max_length=500, blank=True)
    contact_number = models.CharField(max_length=500, blank=True)
    email_id = models.EmailField(blank=True)
    tool_description = models.CharField(max_length=150, blank=True)
    rent_price = models.FloatField(blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.task
