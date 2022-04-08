from django.shortcuts import render

# Create your views here.

def rec(request):
    if request.method=="GET":
        return render(request,"recur.html")
    else:
        r=request.POST('word')
        e=''
        for i in r:
            if i not in e:
                e+=i
            else:
                e[i]=1

    return render(request,'recur.html',{'result':e})
