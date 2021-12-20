from django.db import models

# Create your models here.
class Contact(models.Model):
    cName = models.CharField(max_length=200)
    cEmail = models.EmailField(max_length=150)
    cSubject = models.CharField(max_length=100)
    cMessage = models.TextField(max_length=500)

    class Meta:
        db_table ="CONTACT"