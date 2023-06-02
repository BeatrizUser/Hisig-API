from django.shortcuts import render, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import *
from .serializers import *
from datetime import date


# Create your views here.
class EmpresaListView(APIView):
    def get(self, request, *args, **kwargs):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

class VagasListView(APIView):
    def get(self, request, *args, **kwargs):
        vagas = Vaga.objects.all()
        serializer = VagasSerializer(vagas, many=True)
        return Response(serializer.data)

class CandidatosListView(APIView):
    def get(self, request, *args, **kwargs):
        candidatos = Candidato.objects.all()
        serializer = CandidatosSerializer(candidatos, many=True)
        return Response(serializer.data)

def dashboard(request):
    candidatos = Candidato.objects.all()
    vagas = Vaga.objects.all()
    vagas_abertas = Vaga.objects.filter(data_encerramento__gte=date.today()).count()
    context = {
        'candidatos': candidatos,
        'vagas_abertas': vagas_abertas,
        'vagas': vagas
    }
    return render(request, 'dashboard.html', context)