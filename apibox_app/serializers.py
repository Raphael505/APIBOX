from rest_framework import serializers
from .models import box
class BoxSerializer(serializers.ModelSerializers):
    class Meta:
        model = box
        fields = ['id', 'nome', 'numero']
        # quero usar todos os campos
        # fields = '__all__'