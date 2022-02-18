from django.db import models
from django.utils import timezone

# Callable to define a custom path to the file upload in MEDIA_ROOT / files/datasource/year/month/day
def upload_file_path(instance, filename):
    
    return '/'.join(['uploads',str(filename)])

def getfilename():

    return 'Anonymous File'

class FileDocument(models.Model):

    file_id = models.BigAutoField(primary_key= True)
    
    name = models.CharField(max_length=100, default=getfilename, null=True)

    file = models.FileField(upload_to= upload_file_path)

    content_type = models.CharField(max_length=100, null= True)

    upload_on = models.DateTimeField(default= timezone.now)
