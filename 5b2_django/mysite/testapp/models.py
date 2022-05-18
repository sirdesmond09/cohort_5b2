from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=250, unique=True)
    price = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    # class Meta:
    #     ordering = ["-id"]
    