"""
   HTTP -> Hypertext Transfer Protocol
   HTTPS -> Hypertext transfer Protocol Secure
   JJSON -> JavaScripts Object Notation
   https://ww.w3schools.com/js/js__json.asp
"""

from rest_framework import viewsets
from .models import box
from .serializers import BoxSerializer

class BoxViewSet(viewsets.ModelViewSet):
    queryset = box.objects.all()
    serializer_class = BoxSerializer