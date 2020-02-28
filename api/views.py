from django.shortcuts import render
from rest_framework.generics import CreateAPIView ,RetrieveAPIView ,ListAPIView
from .serializers import RegisterSerializer , ItemListSerializer ,ItemDetailSerializer
from items.models import Item
from rest_framework.permissions import AllowAny
from .permissions import IsOwner
from rest_framework.filters import SearchFilter, OrderingFilter


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer

class ItemListView(ListAPIView):
    queryset = Item.objects.all().order_by("id")
    serializer_class = ItemListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter,]
    search_fields = ['name']

class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [ IsOwner]
