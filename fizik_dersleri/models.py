from django.db import models

class Ders(models.Model):
    ad=models.CharField(max_length=200)   #Dersin adı
    aciklama=models.TextField()           #Dersin açıklaması
    
    def __str__(self):
        return self.ad
