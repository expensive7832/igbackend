from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import userSerializer

@api_view(['POST'])
def Signup(request):

    try:
        data = request.data

        newuser = userSerializer(data=data)

        if newuser.is_valid():
            newuser.save()
        
            output = {
            "message": "signup successfully",
            "data": newuser.data
            }

            return Response(data= output, status=status.HTTP_201_CREATED)
        else:
            return Response(data=newuser.errors, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


    except BaseException as e:
        return Response(data= str(e) )












