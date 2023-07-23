from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class fileUpload(models.Model):
    name = models.CharField(max_length=300)
    text = models.CharField(max_length=1000000000,default="")
    file = models.FileField(upload_to="archives/", default="")
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'file'

    def __str__(self):
        return self.name
