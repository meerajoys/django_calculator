from django.shortcuts import render

from django.http import HttpResponse
from mathsapp.forms import OperationForm,CubeForm,SquareForm,EbillForm
from django.views.generic import View

# Create your views here.
class AddView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'add.html',{'form':form})
    def post(self,request):
        print(request.POST)
        num1 = request.POST["num1"]
        num2 = request.POST["num2"]
        res = int(num1) + int(num2)
        return render(request, "add.html", {"result": res})
class SubView(View):
    def get(self,request):
        form = OperationForm()
        return render(request, "sub.html", {'form': form})
    def post(self,request):
        print(request.POST)
        num1 = request.POST["num1"]
        num2 = request.POST["num2"]
        res = int(num1) - int(num2)
        return render(request, "sub.html", {"result": res})

def add(request):
    if request.method=="GET":
        form=OperationForm()
        return render(request,"add.html",{'form':form})
    else:
        print(request.POST)
        num1=request.POST["num1"]
        num2=request.POST["num2"]
        res=int(num1)+int(num2)
        return render(request,"add.html",{"result":res})       # to print result in front end
def sub(request):
    if request.method=="GET":
        form=OperationForm()
        return render(request,"sub.html",{'form':form})
    else:
        print(request.POST)
        num1=request.POST["num1"]
        num2=request.POST["num2"]
        res=int(num1)-int(num2)
        return render(request,"sub.html",{"result":res})
def mult(request):
    if request.method=="GET":
        form=OperationForm()
        return render(request,"mult.html",{'form':form})
    else:
        print(request.POST)
        num1=request.POST["num1"]
        num2=request.POST["num2"]
        res=int(num1)*int(num2)
        return render(request,"mult.html",{"result":res})
def div(request):
    if request.method=="GET":
        form=OperationForm()
        return render(request,"div.html",{"form":form})
    else:
        print(request.POST)
        num1=request.POST["num1"]
        num2=request.POST["num2"]
        res=int(num1)%int(num2)
        return render(request,"div.html",{"result":res})

def word_count(request):
    if request.method=="GET":
        return render(request,"wordcount.html")
    else:
        text=request.POST["words"]
        wc={

        }
        words=text.split(" ")
        for word in words:
            if word in wc:
                wc[word]+=1
            else:
                wc[word]=1
        return render(request,"wordcount.html",{"result":wc})

def cube(request):
    if request.method=='GET':
        form=CubeForm()
        return render(request,'cube.html',{'form':form})
def square(request):
    if request.method=='GET':
        form=SquareForm()
        return render(request,'square.html',{'form':form})
def home(request):
    return render(request,'home.html')

def ebill(request):
    form=EbillForm()
    return render(request,"ebill.html",{'form':form})
