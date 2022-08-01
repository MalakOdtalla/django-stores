from django.db import models

from django.contrib.auth import get_user_model

from django.urls import reverse

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length= 64)
    description = models.TextField( blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"


    def get_absolute_url(self):
        return reverse('Store_detail')