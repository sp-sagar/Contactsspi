from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions
# Create your views here.
class ContactsList(ListCreateAPIView):

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def prform_create(self, serialiser):
        serializer.save(owner=self.request.user)

    def get_queryset(self):

        return Contact.objects.filter(owner=self.request.user)

class ContactsDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated)
    lookup_field = "id"

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
