from django.db import models

# Create your models here.
class UserData(models.Model):
    name=models.CharField(max_length=20)
    identitycard=models.IntegerField()
    age=models.IntegerField()
    bmi=models.FloatField()
    glucouse=models.FloatField()
    insuline=models.FloatField()
    homa=models.FloatField()
    leptin=models.FloatField()
    adiponcetin=models.FloatField()
    resistiin=models.FloatField()
    mcp=models.FloatField()
    classification=models.CharField(max_length=10)


    def _str__(self):
        return self.name