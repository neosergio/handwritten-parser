from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer


@api_view(['GET'])
def document_list(request):
    documents = Document.objects.all()
    serializer = DocumentSerializer(documents, many=True)
    data = {
        "documents": serializer.data
    }
    response = {"data": data}
    return Response(response, status=status.HTTP_200_OK)
