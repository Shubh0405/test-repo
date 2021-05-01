from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status,views,permissions
from .serializers import *
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def RegistrationAPIView(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
