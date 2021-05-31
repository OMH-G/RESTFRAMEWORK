from django.http import JsonResponse
from django.views.generic.list import ListView
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Scheme_serializer
from mftool import Mftool
from .models import Scheme
General=Mftool()
store_info=General.get_scheme_codes()
# Create your views here.
@api_view(['GET'])
def Overview(request):
    params={
        '<code>/details':'Details of that corresponding scheme code',
        '<code>/short_info':'short information of that corresponding scheme code',
        'list-view-api':'Gives the list of all the scheme codes and short info',
    }
    return Response(params)#Returning the dictionary response as it is from restframework it will go into the api format
@api_view(['GET'])
def short_info(request,b):
    return Response({b:store_info[str(b)]})
@api_view(['GET'])
def details(request,a):
    return Response(General.get_scheme_details(a))

class Listing_Details(APIView):
    def get(self,request):
        a=Scheme.objects.all()
        serialized=Scheme_serializer(a,many=True) 
        return Response(serialized.data)

