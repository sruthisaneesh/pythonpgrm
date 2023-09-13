from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models  import Film
from .forms import Filmform
# Create your views here.
def index(request):
    a=Film.objects.all()
    context={
        'filmlist':a
    }
    return render(request,'index.html',context)

def detail(request,filmid):
    b=Film.objects.get(id=filmid)

    return render(request,'detail.html',{'xy':b})

def addfilm(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        year=request.POST.get('year',)
        descrptn=request.POST.get('descrptn',)
        Image=request.FILES['Image']
        film=Film(name=name,year=year,descrptn=descrptn,Image=Image)
        film.save()
    return render(request,'add.html')

def update(request,id):
    film=Film.objects.get(id=id)
    form=Filmform(request.POST or None,request.FILES,instance=film)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'film':film})


def delete(request,id):
    if request.method=='POST':
        film=Film.objects.get(id=id)
        film.delete()
        return redirect('/')
    return render(request,'delete.html')
