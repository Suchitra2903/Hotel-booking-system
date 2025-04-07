from django.shortcuts import render, redirect


# Create your views here.
from hoteladmin.forms import AdminForm
from hotelmanagement.models import RequestModel


def adminpage(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return redirect('uploadpage')

    return render(request,'hoteladmin/adminpage.html')

def uploadpage(request):
    if request.method == "POST":
        forms = AdminForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('uploadpage')

    else:
        forms = AdminForm()

    return render(request,"hoteladmin/uploadpage.html", {'form': forms})
def viewuserrequest(request):
    obj=RequestModel.objects.all()
    return render(request,'hoteladmin/viewuserrequest.html',{'objects':obj})

def accept(request,pk):
    obj=RequestModel.objects.get(id=pk)
    obj.requeststatus = "VACANT(on hold upto 24 hrs)"
    obj.save(update_fields=["requeststatus"])
    return redirect('viewuserrequest')

def reject(request,pk):
    obj=RequestModel.objects.get(id=pk)
    obj.requeststatus = "NO VACANCY"
    obj.save(update_fields=["requeststatus"])
    return redirect('viewuserrequest')

def adlogout(request):
    return redirect('adminpage')


