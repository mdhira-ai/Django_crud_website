from django.db import models

# Create your models here.
class USER_DATA(models.Model):
    u_name=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.u_name)