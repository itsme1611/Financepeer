from rest_framework import serializers
from fileupload.models import FileDocument

class FileDocumentSerializer(serializers.ModelSerializer):

    name = serializers.CharField(read_only= True)
    content_type = serializers.CharField(read_only= True)
    upload_on = serializers.DateTimeField(read_only= True)
    
    class Meta:

        model = FileDocument
        fields = '__all__'

