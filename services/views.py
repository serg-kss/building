from django.shortcuts import render

# Create your views here.
def services(request):
    return render(request, 'services/services.html')

def service(request):
    return render(request, 'services/service.html')
