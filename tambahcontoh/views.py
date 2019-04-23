from django.shortcuts import render,redirect
from .models import InsertTmbh
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def send(request):
    # print(request)
    # aksi = Foo.objects.create(number1='test',number2=,total=)
    data = InsertTmbh(number1=request.POST['jum1'], number2=request.POST['jum2'],total=request.POST['total'])
    data.save()

    return redirect('/home')
