from django.db import models

# Create your models here.
class food(models.Model):

    fid=models.IntegerField()
    fname=models.CharField(max_length=50)
    fprice=models.IntegerField()
    fquantity=models.IntegerField()
    fdescription=models.TextField()
    fcost=models.IntegerField()

    class Meta:
        db_table='food'
        
