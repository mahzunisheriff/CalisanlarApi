from django.shortcuts import render
from rest_framework.views import APIView
from adresler.models import Adresler
from adresler.serializer import AdreslerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Create your views here.

class AdreslerView(APIView):

    def post(self, request, *args, **kwargs):

        data = request.data

        serializer = AdreslerSerializer(data=data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, *args, **kwargs):
        try:

            adres = Adresler.objects.get(pk=pk)

        except Adresler.DoesNotExist:

            return Response({'error:': 'Adres bulunamadı.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AdreslerSerializer(adres, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, *args, **kwargs):

        adresler = Adresler.objects.all()

        serializer = AdreslerSerializer(adresler, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk, *args, **kwargs):

        try:
            
            adres = Adresler.objects.get(pk=pk)

        except Adresler.DoesNotExist:

            return Response({'error:': 'Adres bulunamadı.'}, status=status.HTTP_404_NOT_FOUND)
        
        adres.delete()

        return Response(status=status.HTTP_200_OK)
    

class CreateAdresView(generics.CreateAPIView):
    queryset = Adresler.objects.all()
    serializer_class = AdreslerSerializer

class UpdateAdresView(generics.UpdateAPIView):
    queryset = Adresler.objects.all()
    serializer_class = AdreslerSerializer

class DeleteAdresView(generics.DestroyAPIView):
    queryset = Adresler.objects.all()
    serializer_class = AdreslerSerializer

class ListAdresView(generics.ListAPIView):
    queryset = Adresler.objects.all()
    serializer_class = AdreslerSerializer

class GetByIdView(generics.RetrieveAPIView):
    queryset = Adresler.objects.all()
    serializer_class = AdreslerSerializer