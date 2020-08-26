from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Document


class DocumentsTestCase(APITestCase):
    def setUp(self):
        self.document_01 = Document.objects.create(text='lorem ipsum')
        self.document_02 = Document.objects.create(text='foo bar')

    def test_document_list(self):
        document_list_url = reverse("document_list")
        response = self.client.get(document_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
