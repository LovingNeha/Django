import re
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def kane(request):
    template='FirstApp/vn.html'
    ob=Employee.objects.all()
    context={
        'a':ob
    }
    return render(request,template,context)

@login_required()
def empdetail(request,pk):
    qs=Employee.objects.get(id=pk)
    template="FirstApp/empdetail.html"
    return render(request,template,{"qs":qs})   

@login_required()
def empdelete(request,pk):
    qs=Employee.objects.get(id=pk)
    qs.delete()
    return redirect("kane")

@login_required()
def emp_form(request):
    form=EmployeeForm(request.POST)
    if form.is_valid():
        abcd=form.save(commit=False)
        abcd.save()
        return redirect("kane")
    template="FirstApp/emp_form.html"
    return render(request,template,{'form':form})    

@login_required()
def emp_update(request,pk):
    qs=get_object_or_404(Employee,pk=pk)
    if request.method=="POST":
        form=EmployeeForm(request.POST, instance=qs)
        if form.is_valid():
            abcd=form.save(commit=False)
            abcd.save()
            return redirect("kane")
    else:
        form=EmployeeForm(instance=qs)
    template="FirstApp/emp_form.html"    
    return render(request,template,{'form':form})   