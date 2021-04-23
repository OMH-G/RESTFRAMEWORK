from rest_framework import serializers
from . models import StreamerName,Video

class JStreamerName(serializers.ModelSerializer):
    v_obj=serializers.StringRelatedField(many=True)
    class Meta:
        model=StreamerName 
        fields=['name','quality','v_obj']