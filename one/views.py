from django.shortcuts import render, redirect
import os
from .forms import ImagePDF

# Create your views here.
from pathlib import Path
import time
wallet=[1]
def index(request):
    form=wallet[0]
    return render(request, 'index.html',{'form':form})




def donateclicked(request):
    
    print('donateclicked')
    for i in range(28):
        
        time.sleep(5)
        print(i)
        last=wallet[0]
        new=last-1
        wallet.insert(0,new)
        print(wallet[0])
    return render(request, 'index.html')
    


    
def funds(request):
    return render(request, 'funds.html',{'form':ImagePDF()})


def add(request):
    mon=request.GET['money']
    wallet.insert(0,int(mon))
    print(f"the money is {mon}")
    return render(request, 'added.html')
