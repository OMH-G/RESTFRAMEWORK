from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse
from .models import StreamerName,Video
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import StreamerName 
from . serializers import JStreamerName
# Create your views here.
def Index(request):
    context={'s':StreamerName.objects.all()}
    return render(request,'index.html',context)
def NameVideo(request,s):
    try:
        name=StreamerName.objects.get(id=s)
    except(KeyError,StreamerName.DoesNotExist):
        return render(request,'index.html',context)
    else:
        # return render(request,'index.html',{'s':Streamer.objects.all(),'id':name.id})
        return render(request,'new.html',{'take':name.videos_set.all()})
@api_view(['GET'])
def Overview(request):
    overview={
        'create':'app-create/',
        'update':'app-update/id',
        'delete':'app-delete/id',
        'Read':'app-list'
    }
    return Response(overview)
@api_view(['GET'])
def list_(request):
    the_data=StreamerName.objects.all()
    serial=JStreamerName(the_data,many=True)
    return Response(serial.data)
@api_view(['POST'])
def create(request):
    serial=JStreamerName(data=request.data)
    if serial.is_valid():
        serial.save()
        return Response(serial.data,status=status.HTTP_201_CREATED)
    return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def update(request,id):
    try:
        get_object=StreamerName.objects.get(id=id)
        serial=JStreamerName(instance=get_object,data=request.data)
        if(serial.is_valid()):
            serial.save()
        return Response(serial.data,status=status.HTTP_201_CREATED)
    except StreamerName.DoesNotExist:
        return Response('There is no ID like that')
    # return Response(serial.data,status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete(request,id):
    try:
        get_object=StreamerName.objects.get(id=id)
        get_object.delete()
        return Response('All ready deleted')
    except StreamerName.DoesNotExist:
        return Response('All ready deleted')
    
# class Echo(APIView):
#     def get(self,request):
#         get_all_objects=StreamerName.objects.all()
#         json_data=JStreamerName(get_all_objects,many=True)
#         print(json_data)
#         # print(json_data.Meta())
#         return Response(json_data.data)
#     def post(self,request):
#         take=JStreamerName(data=request.data) 
#         if(take.is_valid()):
#             print(list(take.validated_data.items()))
#             take.save()
#             return Response(take.data,status=status.HTTP_201_CREATED)
#         return Response(take.errors,status=status.HTTP_400_BAD_REQUEST)
#     def update(self,request,id):
#         take=StreamerName.objects.get(id=id)
#         serial=JStreamerName(instance=take,data=request.data)
#         if(serial.is_valid()):
#             serial.save()
#             return Response(take.data,status=status.HTTP_201_CREATED)
#         return Response(take.errors,status=status.HTTP_400_BAD_REQUEST)
#             # store=StreamerName.objects.filter(name__startswith=list(take.validated_data.items())[0][1])
        
#     def delete(self,request,id):
#         take=StreamerName.objects.get(id=id)
#         # serial=JStreamerName(data=request.data)
#         if(take.is_valid()):
#             take.delete()
#             return Response(take.data,status=status.HTTP_201_CREATED)
#         return Response(take.errors,status=status.HTTP_400_BAD_REQUEST)