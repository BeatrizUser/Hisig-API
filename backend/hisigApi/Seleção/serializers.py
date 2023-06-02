from rest_framework import serializers
from .models import *

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class VagasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'

class CandidatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = '__all__'

# PARA ESPECIFICAR OS CAMPOS A SEREM EXIBIDOS NA API E SÓ POR ELES NUMA ARRAY EM FIELDS