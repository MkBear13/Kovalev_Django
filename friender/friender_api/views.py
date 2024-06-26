from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from friender.models import HotelOwner, Hobbies
from .serializers import HotelOwnerSerializer, HobbiesSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication

class HotelOwnerListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = HotelOwner.objects.all()
    serializer_class = HotelOwnerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["sex", "age"]
    search_fields = ["sex", "age"]
    # def get(self, request):
    #     owners = HotelOwner.objects.all()
    #     serializer = HotelOwnerSerializer(owners, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = HotelOwnerSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelOwnerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = HotelOwner.objects.all()
    serializer_class = HotelOwnerSerializer
    # def get_object(self, pk):
    #     try:
    #         return HotelOwner.objects.get(pk=pk)
    #     except HotelOwner.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk):
    #     owner = self.get_object(pk)
    #     serializer = HotelOwnerSerializer(owner)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     owner = self.get_object(pk)
    #     serializer = HotelOwnerSerializer(owner, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     owner = self.get_object(pk)
    #     owner.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class HobbiesListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    hobbies = Hobbies.objects.all()
    serializer = HobbiesSerializer(hobbies, many=True)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["name", "experience"]
    search_fields = ["name", "experience"]
