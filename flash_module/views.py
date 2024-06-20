from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from  django.shortcuts import get_object_or_404

from flash_module.models import FlashCard
from flash_module.serializers import CreateProfileModelSerializer, CreateFlashCardModelSerializer, \
    UpdateFlashCardModelSerializer, ListFlashCardModelSerializer



class CreateProfileApiView(APIView):
    def post(self,request):
        req_data = request.data
        serializer = CreateProfileModelSerializer(data= req_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # user_data = User(
        #     username = data['username'],
        #     email = data['email']
        # )
        # user_data.set_password(data['password'])
        # user_data.save()
        return Response(serializer.data)

class CreateFlashCardApiView(APIView):
    def post(self,request):
        req_data = request.data
        serializer = CreateFlashCardModelSerializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)

class UpdateFlashCardApiView(APIView):
    def put(self,request,id):
        card_object = get_object_or_404(FlashCard,id= id)
        serializer = UpdateFlashCardModelSerializer(instance=card_object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

class DeleteFlashCardApiView(APIView):
    def delete(self,request,id):
        card_object = get_object_or_404(FlashCard,id = id)
        card_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListFlashCardApiView(APIView):
    def get(self, request):
        card_object = FlashCard.objects.all()
        serializer = ListFlashCardModelSerializer(card_object,many=True)

        return Response(serializer.data,status= status.HTTP_200_OK)

