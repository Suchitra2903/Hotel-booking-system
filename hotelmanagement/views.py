from django.shortcuts import render, redirect

from hoteladmin.models import AdminModel
from hotelmanagement.forms import RegisterForm
from hotelmanagement.models import UserRegistration, RequestModel


def index(request):
    if request.method == "POST":
        usid = request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = UserRegistration.objects.get(firstname=usid, password=pswd)
            request.session['userid'] = check.id
            return redirect('home')
        except:
            pass

    return render(request,'hotelmanagement/index.html')

def register(request):
    if request.method == "POST":
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')

    else:
        forms = RegisterForm()

    return render(request,"hotelmanagement/register.html",{'form':forms})

def home(request):
    return render(request,'hotelmanagement/home.html')


def viewdetails(request):
    obj=AdminModel.objects.all()
    return render(request,'hotelmanagement/viewdetails.html',{'objects':obj})


def singlewithac(request):
    obj=AdminModel.objects.filter(roomcategory='single', actype='with ac' )
    return render(request,'hotelmanagement/singlewithac.html',{'objects':obj})

def singlewithoutac(request):
    obj=AdminModel.objects.filter(roomcategory="single", actype='without ac')
    return render(request,'hotelmanagement/singlewithoutac.html',{'objects':obj})

def doublewithac(request):
    ob=AdminModel.objects.filter(roomcategory="double", actype='with ac')
    return render(request,'hotelmanagement/doublewithac.html',{'object':ob})

def doublewithoutac(request):
    ob=AdminModel.objects.filter(roomcategory="double", actype='without ac')
    return render(request,'hotelmanagement/doublewithoutac.html',{'object':ob})
def userrequest(request,pk):
    userid=request.session['userid']
    userObj=UserRegistration.objects.get(id=userid)
    gymObj=AdminModel.objects.get(id=pk)
    RequestModel.objects.create(userId=userObj,hotel=gymObj)
    return redirect('singlewithac')

def mydetails(request):
    obj = RequestModel.objects.all()
    return render(request,'hotelmanagement/mydetails.html',{'objects':obj})

def logout(request):
    return redirect('index')

