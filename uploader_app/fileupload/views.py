from rest_framework import views, response
from fileupload.models import FileDocument
from fileupload.serializers import FileDocumentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class FileDocumentUpload(views.APIView):

    serializer_class = FileDocumentSerializer
    queryset = FileDocument.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):

        if request.data and 'file' in request.data:

            uploaded_file  = request.data['file']

            new_file = FileDocument.objects.create(
                    name=uploaded_file.filename,
                    file= uploaded_file,
            )

            new_file.save()

            return response.Response({'File uploaded Suceesfully'}, status=200)

        else:

            return response.Response({'FILE NOT SELECTED'}, status=200)