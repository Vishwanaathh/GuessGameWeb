from django.http import HttpResponse
import random
from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def give(request):
    num=random.randint(1,6)
    if(num==int(request.GET["number"])):
         result="You guessed correctly!"
    
    else:
        result="Wrong guess try again!"
    

    return render(request,'number.html',{"number":result,"anum":num})