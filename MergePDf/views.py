import json
from pydoc import describe
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from MergePDf.models import modelA, modelB
from MergePDf.serializers import ModelASerializer
from argparse import ArgumentParser
import contextlib
import PyPDF2

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def merge(request):
    list=[]
    file = request.FILES.getlist('file')
    for index, value in enumerate(file):
        file = f'file{index}' 
        file = value
        list.append(file)
    #for i in list:
        #print(i)
        
    with contextlib.ExitStack() as stack:
        pdfMerger = PyPDF2.PdfFileMerger()
        #files = [stack.enter_context(open(pdf, 'rb')) for pdf in list]
        for f in list:
            pdfMerger.append(f)
        with open('demofile.pdf', 'wb') as f:
            pdfMerger.write(f)
        
    return Response(
        status = 200,
    )

@api_view(['POST'])
@permission_classes([AllowAny])
def data_post(request):
    name = request.data.get('name', None)
    lastname = request.data.get('lastname', None)
    describe = request.data.get('describe', None)
    
    opening = request.data.get('opening', None)
    
    if type(describe) == str:
        de= describe.replace("'", '"')
        describe = json.loads(de)
        

    for i in describe:
        #print(i['id'])
        if i['des'] == 'abc':
            print(i['id'])
            i['id'] = 122
            print(i['id'])
    
    print(type(opening))    
    # if type(opening) == str:
    #     de= opening.replace("'", '"')
    #     opening = json.loads(de)
        
    # for i in opening:
    #     print(i)
    
    dat= modelA.objects.create(
        name=name,
        lastname=lastname
        )
    
    serializer = ModelASerializer(dat)
    
    return Response({
        'data': serializer.data
    })

    