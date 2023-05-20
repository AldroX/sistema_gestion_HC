from typing import Any
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout,authenticate
from .models import Paciente
from .forms import PacienteForm
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, TemplateView


#vista principal 
class home(TemplateView):
    template_name = 'home.html'



#Gestion de Usuarios 
class UsuarioListView(ListView):
    model = User
    template_name = 'Usuarios/Listar_Usuarios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        return context  
    
class UsuarioCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'Usuarios/CrearUsuario.html'
    success_url = reverse_lazy('listarUsuarios')
    
    def post(self,request,*args, **kwargs) :
        dataUser = {}
        try:
          actionU = request.POST['actionU']
          if actionU == 'add':
             form = self.get_form()
             if form.is_valid():
                  form.save()
             else:
                 dataUser['error'] = form.errors
          else:
              dataUser['error'] = 'No ha ingresado a ninguna opcion'

          
        except Exception as alias:
           dataUser['error'] = str(alias)
           
        return JsonResponse(dataUser)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Usuarios'
        context['listarU_urls'] = reverse_lazy('listarUsuarios')
        context['actionU'] = 'add'
        return context

def cerrar(request):
    logout(request)
    return redirect('home')

def Autenticar(request):
    if request.method == 'GET':
     
     return render(request,'log/login.html', {
        'form':AuthenticationForm
    })
    else:
        user = authenticate(request,username=request.POST['username'],
                            password=request.POST['password'])
        
        if user is None:
          return render(request,'log/login.html', {
          'form':AuthenticationForm,
          'error':"Usuario o contraseña incorrecta"

            })
        else:
           login(request,user)
           return redirect('home')




#Gestion de Pacientes -----------------------------------------------    

class PacienteListView(ListView):
   model= Paciente
   form_class = PacienteForm
   template_name='Paciente/Listar_Paciente.html'
  
#    def get_queryset(self):
#        return self.model.objects.filter(estado = True)
   
#    def get_context_data(self,**kwargs):
#        contexto = {}
#        contexto['paciente'] = self.get_queryset()
#        contexto['form'] = self.form_class
#        return contexto
   
#    def get(self,request,*args,**kwargs):
#        return render(request,self.template_name,self.get_context_data())
   
   
   def post(self,request,*args,**kwargs):
       form = self.form_class(request.POST)
       if form.is_valid():
           form.save()
           return redirect('listarPaciente')
           
    

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'Paciente/Modal_CrearPaciente.html'
    success_url = reverse_lazy('listarPaciente') 
    
   
    
    
class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'Paciente/Modal_Paciente.html'
    success_url = reverse_lazy('listarPaciente') 

    def post(self, request, *args, **kwargs):
        context = super().post(request,**kwargs)
        context['paciente'] = Paciente.objects.filter(estado = True)
        return context
        

   
class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'Paciente/Modal.EliminarPaciente.html'
    success_url = reverse_lazy('listarPaciente')

    # def post(self, request,pk, *args, **kwargs):
    #     object = Paciente.objects.get(id = pk)
    #     object.estado = False
    #     object.save()
    #     return redirect('listarPaciente')

        
 
 
 #End Gestion de Pacientes---------------------------------------------  