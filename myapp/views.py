from django.shortcuts import render,redirect
from . models import registerModel,ProductAdding
from . forms import ProductAddingForms,RegistrationAddingForm


def home(request):
    if request.method == "POST":
        name= request.POST.get("user")
        password= request.POST.get("password")

        data= registerModel(username=name, password=password)
        if data is not None:
            return redirect("dashboard")
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

def registration(request):
    if request.method == "POST":
        fullname =request.POST.get("fullname")
        username=request.POST.get("username")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        gender=request.POST.get("gender")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        image=request.FILES.get("image")


        mydata =registerModel(
            fullname=fullname,
            username=username,
            email=email,
            phone=phone,
            gender=gender,
            password=password,
            image=image
            )

        mydata.save()
        print("saved")


    return render(request, 'registration.html')


def dashboard(request):
    values=[1,2,3,4,5]
    mydata=registerModel.objects.all()
    return render(request,'dashboard.html',{"data":values,"mydata":mydata})


def update(request,pk):
    data=registerModel.objects.get(id=pk)
    if request.method == "POST":
        data.fullname =request.POST.get("fullname")
        data.username=request.POST.get("username")
        data.email=request.POST.get("email")
        data.phone=request.POST.get("phone")
        data.gender=request.POST.get("gender")
        data.password=request.POST.get("password")
        if request.FILES.get("image"):
            data.image=request.FILES.get("image")
        

        data.save()
        print("saved")
        return redirect("dashboard")

    return render(request,'update.html',{"data":data})


def delete(request,jk):
    data =registerModel.objects.get(id=jk)
    if request.method == "POST":
        data.delete()
        return redirect("dashboard")

    return render(request,"delete.html",{"data":data})


def product11(request):
        
    if request.method== "POST":
        data=ProductAddingForms(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            print("saved")
    return render(request,"product11.html")


def registration22(request):
    if request.method =="POST":
        dataregister=RegistrationAddingForm(request.POST)
        if dataregister.is_valid():
            dataregister.save()
            print("saved")

    else:
        dataregister = RegistrationAddingForm()        

    return render(request,'registration22.html', {"dataregister":dataregister})