from django.urls import path
from tasks.views import  *



urlpatterns = [
  
  path('',home.as_view(),name='home'),
  #Autenticacion -> falta implementar el Logout y resolver problemas a la hora enviar los datos 
  path('log/login/',Autenticar,name="autenticar"),

  #Gestion de Pacientes -> falta  eliminar 
  path('Paciente/Crear_Paciente/',PacienteCreateView.as_view(), name='crearpaciente'),
  path('Paciente/Listar_Paciente/',PacienteListView.as_view(),name='listarPaciente'),
  path('Paciente/edit/<int:pk>/',PacienteUpdateView.as_view(),name='actualizarPaciente'),
  path('Paciente/delete/<int:pk>/',PacienteDeleteView.as_view(),name='eliminarPaciente'),

  #Gestion de Usuarios -> falta modificar y eliminar 
  path('Usuarios/Listar_Usuarios/',UsuarioListView.as_view(),name='listarUsuarios'),
  # path('Usuarios/Crear_Paciente/',Registrar,name="registro"),
  path('Usuarios/CrearUsuario/',UsuarioCreateView.as_view(),name='crearUsuario')
]



