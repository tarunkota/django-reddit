from ..models import Badge
from rest_framework import serializers

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ['name','info','url','uid']
    