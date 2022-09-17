from django.shortcuts import render
from .form import Studenform
from . models import Form, Formvalidation
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def form(request):
    fm = Studenform
    if request.method == 'POST':
        fm = Studenform(request.POST)
        if fm.is_valid():

            # name = fm.cleaned_data['name']
            # mail = fm.cleaned_data['mail']
            # password = fm.cleaned_data['password']
            print('Form validation')
            print('name:',fm.cleaned_data['name'])
            print('Email:',fm.cleaned_data['mail'])
            print('password', fm.cleaned_data['password'])
            print('price', fm.cleaned_data['price'])
            return HttpResponseRedirect('success')
        else:
            fm = Studenform()

            
    ob = Form.objects.all()

    
    context = {'form': fm, 'fd': ob}

    # ab = Formvalidation.objects.all(context)
    return render(request, 'index.html/' , context)


def success(request):
    return render(request,'success.html/')