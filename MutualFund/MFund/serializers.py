from rest_framework import serializers
from  .models import Scheme 
class Scheme_serializer(serializers.ModelSerializer):
    class Meta:
        model=Scheme 
        fields='__all__'