from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClinicSerializer
from .models import Clinic


# Create your views here.
@api_view(['GET'])
def allClinics(request):
    clinics = Clinic.objects.all()
    serializer = ClinicSerializer(clinics, many=True)
    return Response(serializer.data)
# --------------------------------


@api_view(['GET'])
def getClinic(request, id):
    clinique = Clinic.objects.get(id=id)
    serializer = ClinicSerializer(clinique)
    return Response(serializer.data)


# -----------------------------------------
@api_view(['POST'])
def addClinic(request):
    serializer = ClinicSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# -----------------------------------------
@api_view(['PUT'])
def updateClinic(request, id):
    clinique = Clinic.objects.get(id=id)
    serializer = ClinicSerializer(instance=clinique, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# -----------------------------------------
@api_view(['DELETE'])
def delClinic(request, id):
    clinic = Clinic.objects.get(id=id)
    clinic.delete()
    return Response('Clinique supprimer')

