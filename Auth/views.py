from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
User = get_user_model()

class Home(TemplateView):
    template_name = 'home.html'

#from Auth.models import User

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    data = request.data
    
    #pk = data.get("id")
    username = data.get('username', None)
    email = data.get('email', None)
    password = data.get('password', None)
    
    if password:
            user=User.objects.filter(email=email).exists()
            usrname = User.objects.filter(username=username).exists()
            if user or usrname:
                res = {'created': False, 'message': 'User with this email or username already exists!'}

            else:
                if len(password) < 5 :
                    res = {
                    'created':False,
                    'message':'Password is to short!'
                    }
                    return Response(res)
                print('creating',username,email)
                usr=User.objects.create_user(
                    #id = pk,
                    username = username,
                    email=email,
                    password=password,
                    )

                usr.save()
    else:  
        res = {
                    'created':False,
                    'message':'Password not matched!'
                }

    return Response({'Status' : 'Success'})
        
    