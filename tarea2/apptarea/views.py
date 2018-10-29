from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'apptarea/index.html')

def quienessomos(request):
	return render(request,'apptarea/quienessomos.html')

def carta(request):
	return render(request,'apptarea/carta.html')	

def pedidos(request):
	return render(request,'apptarea/pedidos.html')

def sugerencias(request):
	return render(request,'apptarea/sugerencias.html')
	
def resultado(request):
    dato_nombre = request.POST['nombre']
    dato_sugerencia = request.POST['sugerencia']
    dato_email = request.POST['email']
    contexto = {"nombre":dato_nombre, "sugerencia":dato_sugerencia, "email":dato_email}
    return render(request, 'apptarea/resultado.html', contexto)
