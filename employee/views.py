# Create your views here.
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#from rest_framework.views import APIView

from employee.models import Emp
from employee.serializers import EmpSerializer

from employee.forms import UploadFileForm

import json

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = "application/json"
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def emp_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        emps = Emp.objects.all()
        serializer = EmpSerializer(emps, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def emp_detail(request,pk):
    """
    Retrieve, update a code snippet.
    """
    try:
        emp = Emp.objects.get(pk=pk)
    except Emp.DoesNotExist:
        return HttpResponse(status=400)
    
    if request.method == 'GET':
        serializer = EmpSerializer(emp)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmpSerializer(emp, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.error,status=400)
    elif request.method == 'DELETE':
        emp.delete()
        return HttpResponse(status=204)

# Imaginary function to handle an uploaded file.
def handle_uploaded_file(fname,f):
    with open(settings.PROJECT_ROOT+'/media/img/emp_thum/'+fname, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_exempt
def emp_thum(request,pk):
    if request.method == 'POST':
        fname=request.FILES['thum'].name
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(fname, request.FILES['thum'])
            return HttpResponse("Valid form")
        return HttpResponse("in valid form")
    return HttpResponse("Unknown request")
