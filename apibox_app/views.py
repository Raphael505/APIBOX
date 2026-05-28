"""
   HTTP -> Hypertext Transfer Protocol
   HTTPS -> Hypertext transfer Protocol Secure
   JJSON -> JavaScripts Object Notation
   https://ww.w3schools.com/js/js__json.asp
"""

from django.http import JsonResponse
def box(request):
    if request.method == 'GET':
        box_feira={
            'id': 1,
            'nome': 'Loja Infantil Kids Graça',
            'numero': 101,
        }
        return JsonResponse(box_feira)

