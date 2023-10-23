from django.db import models

# Create your models here.
class MySelf(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    nickName=models.CharField(max_length=255,null=True)
    admNo=models.IntegerField(null=True)

    '''def __str__(self):
        return f"{self.firstName} {self.lastName}"'''