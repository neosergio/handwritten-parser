import jellyfish
from google.cloud import vision
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Document, Product
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


@api_view(['POST'])
def document_upload(request):
    image_raw = request.FILES.get('image').read()

    client = vision.ImageAnnotatorClient()
    image = vision.types.Image(content=image_raw)
    response_from_gcp = client.text_detection(image)
    text = response_from_gcp.full_text_annotation.text

    document = Document.objects.create(text=text)
    serializer = DocumentSerializer(document)

    distance_calculation = list()
    products = Product.objects.all()
    if len(products) > 0:
        for product in products:
            levenshtein_distance = jellyfish.levenshtein_distance(text, product.name)
            jaro_distance = jellyfish.jaro_distance(text, product.name)
            distance_calculation.append({
                "product_name": product.name,
                "levenshtein_distance": levenshtein_distance,
                "jaro_distance": jaro_distance})

    response = {
        "data": serializer.data,
        "distance_calculation": distance_calculation
    }
    return Response(response, status=status.HTTP_201_CREATED)
