from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length=50, null=False)
    email=models.EmailField(max_length=100, null=False)
    notes=models.CharField(max_length=500)
    time=models.DateTimeField()


    def __str__(self):
        return self.name