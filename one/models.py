from django.db import models

class imagetopdf(models.Model):
    
    money = models.CharField(max_length=5)
    
    def __str__(self):
        return self.money