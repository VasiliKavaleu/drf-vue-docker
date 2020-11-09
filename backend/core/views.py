from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

from . models import Car
from . serializers import CarSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet


class MyPagination(PageNumberPagination):
    page_size = 15


class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    pagination_class = MyPagination
    
    # def filter_queryset(self, queryset):
    #     for k, v in self.request.query_params.items():
    #         if k == "cursor":
    #             continue
    #         queryset = queryset.filter(**(k, v))
    #     return queryset




