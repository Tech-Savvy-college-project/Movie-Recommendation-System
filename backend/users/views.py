from django.shortcuts import render
from .forms import UserRegistration

# Create your views here.


def showformdata(request):
    fm = UserRegistration(auto_id=True)
    return render(request, 'login/index.html', {'form':fm})