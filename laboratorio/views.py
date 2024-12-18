from django.shortcuts import render
from .models import Laboratorio, Pagina
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect

# Create your views here.

from .forms import LaboratorioFormCreate


def laboratorios(request):
    contexto = {}
    
    pagina = Pagina.objects.get(nombre="laboratorios")
    pagina.incrementar_visitas()
        
    contexto["cuenta_vistas"] = pagina.cuenta_vistas
    contexto["laboratorios"] = Laboratorio.objects.all()
    return render(request, 'laboratorio/laboratorios.html', contexto)


@login_required(login_url="login")
@permission_required('laboratorio.add_laboratorio', login_url="index")
def crear_laboratorio(request):
    contexto = {}
    contexto["form"] = LaboratorioFormCreate()
       
    if request.method == 'GET':
        return render(request, 'laboratorio/crear_laboratorio.html', contexto)
   
    if request.method == 'POST':
       
        form = LaboratorioFormCreate(request.POST)
        contexto["form"] = form
       
        if form.is_valid():
            model_laboratorio = form.instance
            model_laboratorio.save()
           
            messages.success(request, "Laboratorio creado con éxito.")
            return redirect('laboratorios')
           
        else:
            messages.error(request, "Algo ha fallado, revise bien los datos ingresados.")
            return render(request, 'laboratorio/crear_laboratorio.html', contexto)
 
 
@login_required(login_url="login")
@permission_required('laboratorio.change_laboratorio', login_url="index")        
def editar_laboratorio(request, laboratorio_id):
    contexto = {}
    
    laboratorio = Laboratorio.objects.get(id=laboratorio_id)
    
    if request.method == "POST":
        form = LaboratorioFormCreate(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorios')
    else: 
        form = LaboratorioFormCreate(instance=laboratorio)
            
    contexto["form"] = form
    contexto["laboratorio"] = laboratorio        
    
    return render(request, 'laboratorio/editar_laboratorio.html', contexto)


@login_required(login_url="login")
@permission_required('laboratorio.delete_laboratorio', login_url="index")  
def eliminar_laboratorio(request, laboratorio_id):
    contexto = {}
    
    try:
        laboratorio = Laboratorio.objects.get(id=laboratorio_id)
        
    except laboratorio.DoesNotExist as e:
        messages.error(request, f"No existe un laboratorio con id: {laboratorio_id}")
        return redirect('laboratorios') 
    
    if request.method == "POST":
        laboratorio.delete()
        messages.success(request, "Laboratorio eliminado con éxito")
        return redirect('laboratorios')  

    else:
        # BLOQUE GET
        contexto["laboratorio"] = laboratorio
        return render(request, 'laboratorio/eliminar_laboratorio.html', contexto)