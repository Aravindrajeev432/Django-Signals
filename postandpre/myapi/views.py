from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Store
from.serializer import StoreSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class ShowStore(APIView):

    def get(self,request):
        store = Store.objects.all()

        serializer_class = StoreSerializer(store, many=True)

        return Response(serializer_class.data)

    def post(self,request):
        serializer_class = StoreSerializer(data=request.data, many=True)
        if serializer_class.is_valid():
            print("valid")
            serializer_class.save()
            return Response(200)
        else:
            return Response(500)
    def patch(self,request):
        data = request.data
        store = Store.objects.get(id=data['id'])


        serializer_class = StoreSerializer(store,data=request.data,partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(200)

# class UpdateStocks(APIView):
#     def get(self,request):
#         return(200)
#     def post(self,request):
#         serializer_class = StoreSerializer(store, many=True)
