from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def create_template(request):
    name= request.data.get('name', None)
    designation = request.data.get('designation', None)
    perfession = request.data.get('perfession', None)
    
        
