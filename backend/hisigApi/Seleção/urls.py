from django.urls import path
from . import views

app_name = "Seleção"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('empresas/', views.EmpresaListView.as_view()),
    path('candidatos/', views.CandidatosListView.as_view()),
    path('vagas/', views.VagasListView.as_view())
]
