from django.shortcuts import render
from rest_framework import generics
from .models import Profile, ExtraLinks, Store ,User
from .serializers import ExtraLinksSerializer,  ProfileSerializer, StoreSerializer , PublicDataSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import s3client
from rest_framework.permissions import IsAuthenticated
from dotenv import load_dotenv
import os
# Create your views here.
load_dotenv()
class ProfileLinksView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user = request.user
            profileLinks = Profile.objects.get(user = user)
        except Profile.DoesNotExist:
            return Response({'error':'Not Found'} , status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profileLinks)
        return Response(serializer.data , status=status.HTTP_200_OK)
        

    def put(self , request):
        user = request.user
        try:
            profile = Profile.objects.get(user = user)
            if 'file' in request.data:
                imageUploadResponse =  s3client.uploadImage(request.data['file'] , user.username+'_profile')
                if imageUploadResponse != '':
                    request.data['profile_image_url'] = os.getenv('s3bucket')+imageUploadResponse 
            serializer = ProfileSerializer(profile , data=request.data , partial=True)
            if serializer.is_valid():
                serializer.update(profile , serializer.validated_data)
                return Response(serializer.data , status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            request.data['user'] = user.pk
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
            

class ExtraLinksGetPostView(APIView): 
    permission_classes = [IsAuthenticated]
    def get(self , request):
        try:
            user = request.user
            extralinks = ExtraLinks.objects.filter(user=user)
        except ExtraLinks.DoesNotExist:
            return Response({'error':'Not Found'} , status=status.HTTP_404_NOT_FOUND)
        serializer = ExtraLinksSerializer(extralinks , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        user = request.user
        request.data['user'] = user.pk
        serializer = ExtraLinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        

class ExtraLinksPutDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self , request , extralinkid):
        user = request.user
        try:
            extralink = ExtraLinks.objects.get(id = extralinkid , user = user.pk)
        except ExtraLinks.DoesNotExist:
            return Response({'error':'Not Found'} , status=status.HTTP_404_NOT_FOUND)
        request.data['user'] = user.pk
        serializer = ExtraLinksSerializer(extralink , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.update(extralink , validated_data=serializer.validated_data)
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def delete(self , request ,extralinkid):
        user = request.user.pk
        try:
            extralink = ExtraLinks.objects.get(id = extralinkid , user=user)
        except:
            return Response({'error':'Not Found'} , status=status.HTTP_404_NOT_FOUND)
        extralink.delete()
        return Response(status=status.HTTP_200_OK)


class StoreLinksGetPostView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    def get(self , request):
        try:
            user = request.user
            store = Store.objects.filter(user=user)
        except Store.DoesNotExist:
            return Response({'error':'Not Found'} , status=status.HTTP_404_NOT_FOUND)
        serializer = StoreSerializer(store , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        user = request.user
        request.data['user'] = user.pk
        imageUploadResponse =  s3client.uploadImage(request.data['file'] , request.data['title']+"_"+user.username+'_store')
        if imageUploadResponse != '':
            request.data['product_image_url'] = os.getenv('s3bucket')+imageUploadResponse
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class StorePutDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self , request , storeid):
        user = request.user
        try:
            store = Store.objects.get(id = storeid , user = user.pk)
            request.data['user'] = user.pk
        except Store.DoesNotExist:
            return Response({'error':'Not Found'} , status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'error':'Something went wrong'} , status=status.HTTP_400_BAD_REQUEST)
        if 'file' in request.data:
            title = request.data['title'] if 'title' in request.data else store.title
            imageUploadResponse =  s3client.uploadImage(request.data['file'] , title+"_"+user.username+'_store')
            if imageUploadResponse != '':
                request.data['product_image_url'] = os.getenv('s3bucket')+imageUploadResponse 
        serializer = StoreSerializer(store , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.update(store , validated_data=serializer.validated_data)
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def delete(self , request ,storeid):
        user = request.user
        try:
            store = Store.objects.get(id = storeid , user = user.pk)
        except:
            return Response({'error':'Not Found'} , status=status.HTTP_404_NOT_FOUND)
        store.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def getPublicData(request , user):
    try:
        data = User.objects.get(username = user)
    except User.DoesNotExist:
        return Response({'error':'Not Found'} , status=status.HTTP_404_NOT_FOUND)
    serializer = PublicDataSerializer(data , data=request.data)
    if serializer.is_valid():
        print(serializer.validated_data)
    else:
        print('error')
    return Response(serializer.data , status=status.HTTP_200_OK)