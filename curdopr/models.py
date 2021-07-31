from django.db import models

# Create your models here.
class Voters(models.Model):
    name=models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    email=models.EmailField(default="")
    phone=models.CharField(max_length=11)
    city=models.CharField(max_length=30)
    castVote=models.CharField(max_length=15)

    class Meta:
        db_table='votervotes'






