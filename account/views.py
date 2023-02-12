from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def Signup(req):
    return Response(data="i want to signup")













