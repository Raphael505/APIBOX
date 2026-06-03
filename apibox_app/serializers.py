from rest_framework import serializers
from .models import box

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = box
        fields = '__all__'   # ou liste os campos: ['id', 'nome', 'numero']