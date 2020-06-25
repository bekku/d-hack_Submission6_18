from django.db import models

class jsonres_model(models.Model):
    jsonres_nama = models.CharField(blank=False, null=False, max_length=150)
    coment = models.TextField(blank=True)
    age = models.IntegerField(blank=True)
    def __str__(self):
        return self.jsonres_nama
