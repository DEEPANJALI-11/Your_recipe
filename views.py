from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def receipes(request):
    if request.method=="POST":
        data=request.POST
        rec_name=data.get('rec_name')
        rec_desc=data.get('rec_desc')
        rec_image=request.FILES.get('rec_image')
        
        Receipe.objects.create(
            rec_image=rec_image,
            rec_name= rec_name,
            rec_desc= rec_desc,
        )
        return redirect('/receipes/')
    
    queryset=Receipe.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(rec_name__icontains=request.GET.get('search'))        # print(request.GET.get('search'))




    context={'receipes':queryset}
    return render (request, 'res.html',context)

def delete_receipe(request,id):
    queryset= Receipe.objects.get(id=id)
    queryset.delete()
    # return HttpResponse("a")
    return redirect('/receipes/')

def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        rec_name=data.get('rec_name')
        rec_desc=data.get('rec_desc')
        rec_image=request.FILES.get('rec_image')
        queryset.rec_name=rec_name
        queryset.rec_desc=rec_desc
        if rec_image:
            queryset.rec_image=rec_image
        queryset.save()
        return redirect('/receipes/')
    context={'receipes':queryset}
    return render(request ,'update_receipes.html',context)


