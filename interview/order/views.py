from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class EmbargoDateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request: Request, start_date: str, embargo_date: str, *args, **kwargs) -> Response:
        serializer = self.serializer_class(self.get_queryset(start_date, embargo_date), many=True)

        return Response(serializer.data, status=200)

    def get_queryset(self, start_date, embargo_date):
        return self.queryset.filter(start_date__gt=start_date, embargo_date__lt=embargo_date)