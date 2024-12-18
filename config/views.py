from django.shortcuts import render
 
def index(request):
    contexto = {}
    print(request.user.get_all_permissions())
    return render(request, 'index.html', contexto)

